from .models import Astro
from .serializer import AstroSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import subprocess
import os

from .constants import *



class ParallelJobView(APIView):

    def get(self, request):
        articles = Astro.objects.all()
        serializer = AstroSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("[POST] Request - Parallel Jobs")
        input = request.data
        print("Input Received :\n", input)
        serializer = AstroSerializer(data=input)

        if serializer.is_valid():
            serializer.save()
            print("Valid input  data received.")
            udid = input["udid"]
            port = input["port"]
            modulename = input["modulename"]
            platform = input["platform"]

            print("UDID:", udid)
            print("PORT:", port)
            print("MODULE:", modulename)
            print("PLATFORM:", platform)

            curr_dir = os.getcwd()
            git_repo_path = curr_dir.replace('backend', GIT_REPO)                
            print("Git Repo Path:", git_repo_path)
            os.chdir(git_repo_path)
            if platform.__eq__("ANDROID"):
                print("ANDROID  platform selected.")
                cmd = "python3 Runner.py -p True"
            else:
                print("IOS platform selected.")
                cmd = "python3 Runner.py -p True"

            print("Command: ", cmd)
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            data, error = proc.communicate()
            print("Execution Data:", data.decode("utf-8"))
            print("Execution Error:", error.decode("utf-8"))
            print("SERIALIZED DATA: ", serializer.data)

            return Response(serializer.data)

        print("Invaid input json data !!! Please provide the proper data.")
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ScreenshotsView(APIView):

    def get(self, request):
        articles = Astro.objects.all()
        serializer = AstroSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("[POST] Request - Screenshots")
        input = request.data
        print("Input Received:\n", input)
        serializer = AstroSerializer(data=input)

        if serializer.is_valid():
            serializer.save()
            print("Valid input data received.")
            udid = input["udid"]
            port = input["port"]
            modulename = input["modulename"]
            platform = input["platform"]

            print("UDID:", udid)
            print("PORT:", port)
            print("MODULE:", modulename)
            print("PLATFORM:", platform)

            curr_dir = os.getcwd()
            git_repo_path = curr_dir.replace('backend', GIT_REPO)                
            print("Git Repo Path:", git_repo_path)
            os.chdir(git_repo_path)
            if platform.__eq__("ANDROID"):
                print("ANDROID  platform selected.")
                cmd = "python3 Runner.py -s True -pl ANDROID -u {0} -po {1}".format(
                    udid, port)
            else:
                print("IOS platform selected.")
                cmd = "python3 Runner.py -s True -pl IOS -u {0} -po {1}".format(
                    udid, port)

            print("Command:", cmd)
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            data, error = proc.communicate()
            print("Execution Data:", data.decode("utf-8"))
            print("Execution Error:", error.decode("utf-8"))
            print("SERIALIZED DATA: ", serializer.data)

            return Response(serializer.data)

        print("Invaid input json data !!! Please provide the proper data.")
        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PortResetJob(APIView):

    def get(self, request):
        articles = Astro.objects.all()
        serializer = AstroSerializer(articles, many=True)
        print("Port Reset job!!!!!!!!!!!!!")
        print("Astro Automation [GET] method called.")
        print("[GET] SERIALIZED DATA: ", serializer.data)
        print("Trigerring the Astro Automation Job")
        curr_dir = os.getcwd()
        git_repo_path = curr_dir.replace(
            'backend', 'Git_Repo/astro-scorpius-automation-master')
        print("Git Repo Path : ", git_repo_path)
        os.chdir(git_repo_path)
        print("Running...")
        proc = subprocess.Popen("python3 Runner.py -r True ",
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        data, error = proc.communicate()
        print("Execution Data  :", data.decode("utf-8"))
        print("Execution Error :", error.decode("utf-8"))
        content = {'STATUS': 'OK'}
        return Response(content, status=status.HTTP_200_OK)


class AndroidIOSAutomation(APIView):

    def get(self, request):
        articles = Astro.objects.all()
        serializer = AstroSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("[POST] Request Received from the ReactJS Dashboard.")
        input = request.data
        print("Input Received:\n", input)
        serializer = AstroSerializer(data=input)

        if serializer.is_valid():
            serializer.save()
            print("Valid input data received.")
            udid = input["udid"]
            port = input["port"]
            modulename = input["modulename"]
            platform = input["platform"]

            print("UDID:", udid)
            print("PORT:", port)
            print("MODULE:", modulename)
            print("PLATFORM:", platform)

            print("Trigerring the Astro Automation Job")
            curr_dir = os.getcwd()
            git_repo_path = curr_dir.replace(
                'backend', 'Git_Repo/astro-scorpius-automation-master')
            print("Git Repo Path : ", git_repo_path)
            os.chdir(git_repo_path)
            print("Running...")
            if platform.__eq__("ANDROID"):
                print("IOS platform selected.")
                cmd = "python3 Runner.py -pl ANDROID -u {0} -po {1}".format(
                    udid, port)
            else:
                print("ANDROID platform selected.")
                cmd = "python3 Runner.py -pl IOS -u {0}  -po {1}".format(
                    udid, port)

            print("Command:", cmd)
            proc = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            data, error = proc.communicate()
            print("Execution Data  :", data.decode("utf-8"))
            print("Execution Error :", error.decode("utf-8"))
            print("SERIALIZED DATA: ", serializer.data)
            # content = {'STATUS': 'OK'}
            return Response(serializer.data)

        print("Invaid input json data !!! Please provide the proper data.")
        print(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AstroAPIView(APIView):

    def get(self, request):
        articles = Astro.objects.all()
        serializer = AstroSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AstroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Hello world !!!!")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AstroDetails(APIView):

    def get_object(self, id):
        try:
            return Astro.objects.get(id=id)
        except Astro.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = AstroSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = AstroSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
