def receive_messages(project_id: str, subscription_id: str, timeout: float = None) -> None:
    from concurrent.futures import TimeoutError
    from google.cloud import pubsub_v1

    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(project_id, subscription_id)

    def callback(message: pubsub_v1.subscriber.message.Message) -> None:
        print(f"Received {message}.")
        message.ack()

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    with subscriber:
      try:
        streaming_pull_future.result(timeout=timeout)
      except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.

receive_messages("<SEU_PROJETO>","<SEU_TOPICO>") # Altere aqui