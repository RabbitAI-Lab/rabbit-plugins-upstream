# 微信 Agent Pay 商户服务端 - 生产镜像
FROM python:3.11-slim

WORKDIR /app

# 先装依赖（利用 Docker 层缓存）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制服务代码
COPY server.py .

# 不把 .env 打进镜像；运行时通过挂载或环境变量注入
# 如需默认值，可改为 COPY .env.example .env.example

EXPOSE 8080
CMD ["python", "server.py"]
