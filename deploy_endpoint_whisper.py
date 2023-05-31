import asyncio
from trainml import TrainML

client = TrainML()

async def create_endpoint():
    job = await client.jobs.create(
        name="Simple Image Classifier",
        type="endpoint",
        gpu_type="RTX 2080 Ti",
        gpu_count=1,
        disk_size=10,
        model=dict(
            source_type="git",
            source_uri="https://github.com/Sarathharidas/trainml.git",
        ),
        environment=dict(
            type="DEEPLEARNING_PY38",
        ),
        endpoint=dict(
            routes=[
                dict(
                    path="/predict",
                    verb="POST",
                    function="predict_base64_voice",
                    file="predict",
                    positional=True,
                    body=[
                        dict(
                            name="name",
                            type="str",
                        ),
                        dict(name="contents", type="str"),
                    ],
                )
            ]
        ),
    )
    print("Created Job: ", job.id)
    print("Waiting for job to start...")
    await job.wait_for("running")
    print("")
    print("Endpoint running at: ", job.url)
    return job


if __name__ == '__main__':
    asyncio.run(create_endpoint())