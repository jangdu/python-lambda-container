FROM public.ecr.aws/lambda/python:3.12

# optional : pip update
RUN /var/lang/bin/python3.12 -m pip install --upgrade pip

# install git
RUN yum install git -y

# 미리 구성된 github clone
RUN git clone https://github.com/jangdu/python-lambda-container

# install packages
RUN pip install -r python-lambda-container/requirements.txt

# /var/task/ 경로로 실행파일 복사
RUN cp python-lambda-container/lambda_function.py /var/task/
# RUN cp python-lambda-container/imagenet_class_index.json /var/task/

# 실행 시 lambda_function.py의 lambda_handler 함수를 실행시킴을 정의
CMD ["lambda_function.lambda_handler"]