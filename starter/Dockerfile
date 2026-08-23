# GIVEN, real, deliberately flawed -- this is the container image a
# small internal tool uses to run a batch script against your pipeline's
# output. Real security review exercise: find the real issues here and
# propose real fixes in required_components.md Section 4. There is more
# than one real issue -- name all you find, not just one.

FROM python:latest

RUN pip install pandas requests boto3

ENV AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
ENV AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

COPY . /app
WORKDIR /app

CMD ["python", "batch_script.py"]
