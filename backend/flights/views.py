from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse

from .serializers import (
    CountrySerializer,
    AirportSerializer,
    AirplaneModelSerializer,
    AirplaneSerializer,
    AirlineSerializer,
    CrewSerializer,
    CrewMemberSerializer,
    FlightSerializer,
    ReservationSerializer,
    LuggageSerializer,
    UserSerializer
)
from .models import (
    Country,
    Airport,
    AirplaneModel,
    Airplane,
    Airline,
    Crew,
    CrewMember,
    Flight,
    Reservation,
    Luggage
)


@permission_classes([AllowAny])
@api_view(['POST'])
def create_user(request):
    try:
        if (request.data['password1'] != request.data['password2']):
            return HttpResponse("Passwords don't match", status=status.HTTP_400_BAD_REQUEST)
    except:
        return HttpResponse('Data not correct', status=status.HTTP_400_BAD_REQUEST)

    data = {
        'username': request.data['username'],
        'email': request.data['email'],
        'password': request.data['password1']
    }

    user_model = get_user_model()
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        user_model.objects.create_user(
            username=data['username'], email=data['email'], password=data['password'])
        return HttpResponse('User created', status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_username(request):
    username = ''
    try:
        username = request.user.username
    except:
        username = "Error in getting username"
    return JsonResponse({'username': username}, status=status.HTTP_200_OK)


class CountriesList (generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def country_detail(request, country_id):
    try:
        country = Country.objects.get(id=country_id)
    except Country.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CountrySerializer(country)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        country.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class AirportsList (generics.ListCreateAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    # permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def airport_detail(request, airport_id):
    try:
        airport = Airport.objects.get(id=airport_id)
    except Airport.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AirportSerializer(airport)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AirportSerializer(airport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airport.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class AirplaneModelsList (generics.ListCreateAPIView):
    queryset = AirplaneModel.objects.all()
    serializer_class = AirplaneModelSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def airplane_model_detail(request, airplane_model_id):
    try:
        airplane_model = AirplaneModel.objects.get(id=airplane_model_id)
    except AirplaneModel.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AirplaneModelSerializer(airplane_model)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AirplaneModelSerializer(airplane_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airplane_model.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class AirplanesList (generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def airplane_detail(request, airplane_id):
    try:
        airplane = Airplane.objects.get(id=airplane_id)
    except Airplane.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AirplaneSerializer(airplane)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AirplaneSerializer(airplane, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airplane.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class AirlinesList (generics.ListCreateAPIView):
    queryset = Airline.objects.all()
    serializer_class = AirlineSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def airline_detail(request, airline_id):
    try:
        airline = Airline.objects.get(id=airline_id)
    except Airline.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AirlineSerializer(airline)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = AirlineSerializer(airline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        airline.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CrewsList (generics.ListCreateAPIView):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def crew_detail(request, crew_id):
    try:
        crew = Crew.objects.get(id=crew_id)
    except Crew.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CrewSerializer(crew)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CrewSerializer(crew, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        crew.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class CrewMembersList (generics.ListCreateAPIView):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def member_detail(request, member_id):
    try:
        member = CrewMember.objects.get(id=member_id)
    except CrewMember.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CrewMemberSerializer(member)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = CrewMemberSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class FlightsList (generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def flight_detail(request, flight_id):
    try:
        flight = Flight.objects.get(id=flight_id)
    except Flight.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = FlightSerializer(flight)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flight.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class ReservationsList (generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def reservations_list(request):
    if request.method == 'GET':
        queryset = Reservation.objects.all()
        serializer = ReservationSerializer(queryset, many=True)

        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = {
            'user': request.user.username,
            'flight': request.data['flight'],
            'price': request.data['price']
        }
        serializer = ReservationSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def reservation_detail(request, reservation_id):
    try:
        reservation = Reservation.objects.get(id=reservation_id)
    except Reservation.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReservationSerializer(reservation)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = ReservationSerializer(reservation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reservation.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class LuggagesList (generics.ListCreateAPIView):
    queryset = Luggage.objects.all()
    serializer_class = LuggageSerializer
    permission_classes = [IsAuthenticated]


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def luggage_detail(request, luggage_id):
    try:
        luggage = Luggage.objects.get(id=luggage_id)
    except Luggage.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LuggageSerializer(luggage)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = LuggageSerializer(luggage, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        luggage.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
