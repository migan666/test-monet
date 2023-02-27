from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Answer,Question,Test
from .serializers import AnswerSerializer,QuestionSerializer,TestSerializer

class AnswerView(APIView):
    def get(self, request, test_id):
        # Obtener el Test
        test = Test.objects.get(id=test_id)
        test_serializer = TestSerializer(test)
        # Obtener todas las preguntas del Test
        questions = Question.objects.filter(test=test)
        question_serializer = QuestionSerializer(questions, many=True)        
        response_data = test_serializer.data
        response_data['questions'] = question_serializer.data

        return Response(response_data)
    def post(self, request, test_id):
        # Obtener el Test
        test = Test.objects.get(id=test_id)
        # Iterar sobre la lista de respuestas y guardarlas
        for answer_data in request.data:
            # Obtener la pregunta y el usuario asociado con la respuesta
            question = Question.objects.get(id=answer_data['question'])
            user = request.user
            # Crear el objeto de respuesta y guardarla
            answer = Answer(question=question, user=user, answer=answer_data['answer'])
            answer.save()

        return Response({"message": "Respuestas guardadas correctamente"})
