FROM python:3.8.12

# copy files to the /app folder in the container
COPY requirements.txt /app/requirements.txt
COPY Streamlit.py /app/Streamlit.py
COPY api.py /app/api.py
COPY notebooks/supervised.pkl /app/notebooks/supervised.pkl

WORKDIR /app

RUN pip install -r requirements.txt

# execute the command python main.py (in the WORKDIR) to start the app
CMD ["streamlit", "run", "Streamlit.py", "--server.port", "8501"]
