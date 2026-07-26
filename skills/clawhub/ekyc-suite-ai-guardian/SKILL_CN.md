# eKYC Suite AI 守护者

eKYC Suite AI Guardian 是母品牌 `eKYC Suite` 下的独立活体与合成媒体风险检测 Skill，支持照片活体、视频活体、翻拍风险、AI 生成人脸图和 Deepfake 风险检测。

运行：

```bash
python scripts/ai_guardian.py photo --file <人脸照片>
python scripts/ai_guardian.py video --file <人脸视频>
```

检测结果仅作为风险复核信号，不能替代人工判断或直接形成高影响决策。

## 权限与数据流

仅读取用户在命令中明确指定的人脸照片或视频，以及 `EKYC_CLOUD_ENDPOINT`、`EKYC_CLOUD_API_KEY` 两个必要环境变量。媒体会发送到运营方配置的 HTTPS eKYC Suite Cloud 后端进行远程处理。人脸媒体属于敏感生物识别数据，仅可在已获得用户授权、明确留存策略并实施访问控制的情况下处理；公开 Skill 本地不保存媒体或结果。

需求沟通：`carochen112233@gmail.com`
