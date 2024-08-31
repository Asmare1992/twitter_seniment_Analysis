{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "959e398e-829b-4b49-be1e-5a4b2058d3aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from time import sleep\n",
    "import csv \n",
    "from kafka import KafkaProducer\n",
    "import json\n",
    "\n",
    "producer = KafkaProducer(bootstrap_servers=['localhost:9092'],\n",
    "                         value_serializer=lambda x: \n",
    "                         json.dumps(x).encode('utf-8'))\n",
    "\n",
    "with open('twitter_validation.csv') as file_obj:\n",
    "    reader_obj = csv.reader(file_obj)\n",
    "    for data in reader_obj: \n",
    "        # print(data)\n",
    "        producer.send('numtest', value=data)\n",
    "        sleep(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c53d155-4a06-431d-ae40-fa9cd959c7b2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c7d1a4b-858d-443d-a658-ce740a7d297f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2fd86f5-b053-4e31-b42c-8bf84dcae545",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
