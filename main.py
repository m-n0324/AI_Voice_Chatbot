import modal

# 1. Define the App
app = modal.App("my-assistant-app")

# 2. This function will run in the cloud
@app.function()
def cloud_hello():
    print("Hello from the Modal Cloud!")
    return "Cloud execution successful."

# 3. This is the 'entrypoint' that starts the process
@app.local_entrypoint()
def main():
    print("Starting local entrypoint...")
    result = cloud_hello.remote()
    print(result)