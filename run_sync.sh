 #!/usr/bin/env bash

 
# export PYTHONPATH="${PYTHONPATH}:/Users/andrewozor/o/highlight-service-v5/src"
export PYTHONUNBUFFERED=1;

# gunicorn --name=sync-app \
# 	--bind 0.0.0.0:1000 \
# 	--workers=1 src.sync_app:app \
# 	--worker-class=gevent \
# 	--log-level=DEBUG
python src/run_sync.py 