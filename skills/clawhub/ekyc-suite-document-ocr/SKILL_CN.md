# eKYC Suite 证件 OCR

eKYC Suite Document OCR 是母品牌 `eKYC Suite` 下的独立证件 OCR Skill，统一支持身份证、银行卡、驾驶证和行驶证结构化识别。

运行：

```bash
python scripts/document_ocr.py id-card --image <图片> --side 0
python scripts/document_ocr.py bank-card --image <图片>
python scripts/document_ocr.py driver-license --image <图片>
python scripts/document_ocr.py vehicle-license --image <图片> --side 1
```

证件图片和识别结果可能包含敏感个人数据，应进行授权、脱敏、访问控制和留存限制。

## 权限与数据流

仅读取用户在命令中明确指定的证件图片，以及 `EKYC_CLOUD_ENDPOINT`、`EKYC_CLOUD_API_KEY` 两个必要环境变量。证件图片会发送到运营方配置的 HTTPS eKYC Suite Cloud 后端进行远程处理。仅可处理已获授权的证件，并应实施脱敏、最小留存、访问控制和人工复核；公开 Skill 本地不保存图片或结果。

需求沟通：`carochen112233@gmail.com`
