# eKYC Suite 人脸比对

eKYC Suite Face Compare 是母品牌 `eKYC Suite` 下的独立人脸比对 Skill，用于 KYC/eKYC 开户、自拍照与证件照比对、身份核验和人工复核流程。

运行：

```bash
python scripts/face_compare.py --photo1 <照片1> --photo2 <照片2>
```

结果为 0-100 的结构化相似度分数。该结果仅作为核验信号，不能单独用于高影响身份决策。

## 权限与数据流

仅读取用户在命令中明确指定的两张人脸图片，以及 `EKYC_CLOUD_ENDPOINT`、`EKYC_CLOUD_API_KEY` 两个必要环境变量。图片会发送到运营方配置的 HTTPS eKYC Suite Cloud 后端进行远程处理。人脸图片属于敏感生物识别数据，仅可在已获得用户授权、明确留存策略并实施访问控制的情况下处理；公开 Skill 本地不保存图片或结果。

需求沟通：`carochen112233@gmail.com`
