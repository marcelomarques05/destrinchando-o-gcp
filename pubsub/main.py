# Altere o Nome do Projeto e o Tópico
def hello_gcs(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
    Args:
         event (dict): The dictionary with data specific to this type of event.
         context (google.cloud.functions.Context): The Cloud Functions
         event metadata.
    """
    file = event
    print(f"Processing file: {file['name']}.")
    publish_messages("<SEU_PROJETO>","<SEU_TOPICO>") # Atualize as informações aqui.

# Altere a ação que você deseja monitorar
def publish_messages(project_id: str, topic_id: str) -> None:
  from google.cloud import pubsub_v1
  publisher = pubsub_v1.PublisherClient()
  topic_path = publisher.topic_path(project_id, topic_id)
  
  data = "Um arquivo foi adicionado no GCS"
  data = data.encode("utf-8")
  publisher.publish(topic_path, data, gos='<ACAO_A_MONITORAR>') # Exemplo: modify, delete
  
  print(f"Published messages to {topic_path}.")