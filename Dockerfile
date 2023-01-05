FROM python:3.8.10
WORKDIR /usr/src/app/
COPY . /usr/src/app/
RUN apt-get update
RUN pip install pyTelegramBotAPI
RUN pip install openai
RUN pip install asyncio
RUN pip install aiohttp
CMD ["python", "main.py"]