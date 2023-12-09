key = "dc18f5e27339479db330dcfd68312d07"
endpoint = "https://finalprojectyash.cognitiveservices.azure.com/"

import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

client = ConversationAnalysisClient(endpoint, AzureKeyCredential(key))
with client:
    poller = client.begin_conversation_analysis(
        task={
            "displayName": "Analyze conversations from xxx",
            "analysisInput": {
                "conversations": [
                    {
                        "conversationItems": [
                            {
                                "text": "Hello, you’re chatting with Rene. How may I help you?",
                                "id": "1",
                                "role": "Agent",
                                "participantId": "Agent_1",
                            },
                            {
                                "text": "Hi, I tried to set up wifi connection for Smart Brew 300 coffee machine, but it didn’t work.",
                                "id": "2",
                                "role": "Customer",
                                "participantId": "Customer_1",
                            },
                            {
                                "text": "I’m sorry to hear that. Let’s see what we can do to fix this issue. Could you please try the following steps for me? First, could you push the wifi connection button, hold for 3 seconds, then let me know if the power light is slowly blinking on and off every second?",
                                "id": "3",
                                "role": "Agent",
                                "participantId": "Agent_1",
                            },
                            {
                                "text": "Yes, I pushed the wifi connection button, and now the power light is slowly blinking.",
                                "id": "4",
                                "role": "Customer",
                                "participantId": "Customer_1",
                            },
                            {
                                "text": "Great. Thank you! Now, please check in your Contoso Coffee app. Does it prompt to ask you to connect with the machine?",
                                "id": "5",
                                "role": "Agent",
                                "participantId": "Agent_1",
                            },
                            {
                                "text": "No. Nothing happened.",
                                "id": "6",
                                "role": "Customer",
                                "participantId": "Customer_1",
                            },
                            {
                                "text": "I’m very sorry to hear that. Let me see if there’s another way to fix the issue. Please hold on for a minute.",
                                "id": "7",
                                "role": "Agent",
                                "participantId": "Agent_1",
                            },
                        ],
                        "modality": "text",
                        "id": "conversation1",
                        "language": "en",
                    },
                ]
            },
            "tasks": [
                {
                    "taskName": "Issue task",
                    "kind": "ConversationalSummarizationTask",
                    "parameters": {"summaryAspects": ["issue"]},
                },
                {
                    "taskName": "Resolution task",
                    "kind": "ConversationalSummarizationTask",
                    "parameters": {"summaryAspects": ["resolution"]},
                },
            ],
        }
    )

    # view result
    result = poller.result()
    task_results = result["tasks"]["items"]
    for task in task_results:
        print(f"\n{task['taskName']} status: {task['status']}")
        task_result = task["results"]
        if task_result["errors"]:
            print("... errors occurred ...")
            for error in task_result["errors"]:
                print(error)
        else:
            conversation_result = task_result["conversations"][0]
            if conversation_result["warnings"]:
                print("... view warnings ...")
                for warning in conversation_result["warnings"]:
                    print(warning)
            else:
                summaries = conversation_result["summaries"]
                for summary in summaries:
                    print(f"{summary['aspect']}: {summary['text']}")