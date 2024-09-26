# Townsfolks vs werewolves 

![Screenshot 2024-09-26 103016](https://github.com/user-attachments/assets/629e5bbe-5f3f-44d2-856e-7f5351c90389)

## Description
This is a fun simulation comprising of a mixture of mafia and among us. The villagers and werewolves are agents with seperate memories which are implemented using langchain. The Generative AI agents take decisions using opeai's LLM Model and decide to vote out suspicious villagers using their memories.

![Screenshot 2024-09-26 103750](https://github.com/user-attachments/assets/c6bff396-0c62-4382-a549-b57fd8e7ca30)

![Screenshot 2024-09-26 103401](https://github.com/user-attachments/assets/6f62fd3f-3bd1-4a0a-b242-be1151110fa6)



## Installation
1. Clone the repository to your local machine.
2. Run the `requirements.py` script to install the dependencies:
    ```bash
    python requirements.py
    ```

## Usage
1. Create a virtual environment:
    - Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - Windows (PowerShell):
      ```powershell
      python -m venv venv
      .\venv\Scripts\Activate.ps1
      ```

2. Install the project dependencies:
    ```bash
    pip install -r requirements.txt    
    ```

3. Initialize the environment variables by creating a `.env` file based on the provided `.env.example` file.
    ```bash
    cp .env.example .env
    ```

4. Run the game:
    ```bash
    python game.py
    ```
    
## Generative Agent Architecture
### Generative Agents
Generative agents are AI models that simulate human-like behavior, decision-making, and interactions in dynamic environments using memory and learned experiences. Agents are able to interact with each other and the environment, make observations and generate reflections on past memories to gain new insights. Below is the memory architecture of agents.

![agent memory drawio agentmemory](https://github.com/user-attachments/assets/0850de31-95d1-466d-9cac-6fb8e6019625)


![Agent memory architecture](https://github.com/user-attachments/assets/3793b227-0fb9-45a7-adb8-381682d7fe56) 

These agents were able to interact and generate reactions to different observations. Below the mechanism for generating reactions.

![agent vision drawio entity_identification](https://github.com/user-attachments/assets/80b36a44-83ef-40ce-a651-647b2a8632f4)

![agent memory drawio generatereaction](https://github.com/user-attachments/assets/0d54999c-a9c0-44d0-9997-53dcdada801f)

### Villagers
Villagers were inherited from the agent class and modified to match the purpose of the character.
**Purpose :** 
1. Choose tasks to perform based on villagers' occupation and complete them.
2. Hold morning meetings and vote out the werewolf (imposter).
3. Interact with other agents and discuss about the agenda.

![werewolf drawio villager generate_reaction](https://github.com/user-attachments/assets/d1cdfc06-9b34-422f-b1eb-86ca010337ad)

![Screenshot 2024-09-26 103613](https://github.com/user-attachments/assets/f874c3cb-1f3d-4d33-b8f7-18aa7e10e6bc)

### Werewolves
Werewolves were similarly inherited from the agent class but was modified to incorporate the werewolves special ability to eliminate villagers and sabotage tasks.
**Purpose :**
1. Choose tasks to sabotage so that villagers will have to reperform that task.
2. Eliminate villagers when deems fit.
3. Not reveal about being the werewolf (imposter) during morning meets or any discussions with villagers

![werewolf drawio werewolf generate_reaction](https://github.com/user-attachments/assets/a2265e70-3b5b-4a4c-aedc-3b59ae95c602)

![image](https://github.com/user-attachments/assets/efd7bd1c-95e0-401d-a0b1-a953c492ee80)

## Contributing
We welcome contributions! If you'd like to contribute to the project, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

