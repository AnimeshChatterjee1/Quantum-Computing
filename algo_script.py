{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d50992fb-c46e-4ebb-81f4-598af77ab89f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hybrid job started :\n",
      "Counter({'0': 365, '1': 35})\n",
      "Counter({'0': 341, '1': 59})\n",
      "Counter({'1': 341, '0': 59})\n",
      "Counter({'1': 395, '0': 5})\n",
      "Counter({'0': 348, '1': 52})\n",
      "Counter({'1': 400})\n",
      "Counter({'0': 337, '1': 63})\n",
      "T  : |    0    |\n",
      "                \n",
      "q0 : -Rx(-0.90)-\n",
      "\n",
      "T  : |    0    |\n",
      "Test hybrid job completed!\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import numpy as np\n",
    "from braket.devices import LocalSimulator\n",
    "from braket.aws import AwsDevice\n",
    "from braket.circuits import Circuit\n",
    "from braket.jobs import save_job_result\n",
    "from braket.tracking import Tracker\n",
    "\n",
    "t = Tracker().start()\n",
    "\n",
    "print(\"Hybrid job started :\")\n",
    "\n",
    "# Use the device declared in the creation script\n",
    "device = LocalSimulator()\n",
    "\n",
    "counts_list = []\n",
    "angle_list = []\n",
    "for _ in range(7):\n",
    "    angle = np.pi * np.random.randn()\n",
    "    random_circuit = Circuit().rx(0, angle)\n",
    "\n",
    "    task = device.run(random_circuit, shots=400)\n",
    "    counts = task.result().measurement_counts\n",
    "\n",
    "    angle_list.append(angle)\n",
    "    counts_list.append(counts)\n",
    "    print(counts)\n",
    "print(random_circuit)\n",
    "\n",
    "# Save the variables of interest so that we can access later\n",
    "save_job_result({\"counts\": counts_list, \"angle\": angle_list, \"estimated cost\": t.qpu_tasks_cost() + t.simulator_tasks_cost()})\n",
    "\n",
    "print(\"Test hybrid job completed!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "23275510-3625-4eab-b8e2-f847e55f806a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax. Perhaps you forgot a comma? (213476086.py, line 5)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[5], line 5\u001b[0;36m\u001b[0m\n\u001b[0;31m    source_module=\"algo_script.py\"\u001b[0m\n\u001b[0m                  ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6d16e70-9c59-4cd2-bf0b-d8e7f5297108",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "conda_braket",
   "language": "python",
   "name": "conda_braket"
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
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
