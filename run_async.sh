 #!/usr/bin/env bash

# use gunicorn to run the asgi app 
# export PYTHONPATH="${PYTHONPATH}:/Users/andrewozor/o/highlight-service-v5/src"
export PYTHONUNBUFFERED=1;

# gunicorn --name=async-app \
# 	--bind 0.0.0.0:5000 \
# 	--workers=1 \
# 	--worker-class=uvicorn.workers.UvicornWorker \
# 	--log-level=DEBUG \
# 	src.async_app:app

# python -X dev src/disco/highlight_service/run.py 
python src/run_async.py 
