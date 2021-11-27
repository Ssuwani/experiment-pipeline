# Katib 를 통해 수행하는 실험 파이프라인

**Diagram**

<img src="images/diagram.png"/>

**순서도**

1. 개발자 `train.py` 를 Github Repository에 Push
2. Github Action을 통해 수행되는 Docker build & push
3. ArgoCD가 바라보고 있는 Deploy Repository Update with tag
4. ArgoCD가 Kubernetes에 `train-experiment.yaml` 실행 
5. Slack Alert