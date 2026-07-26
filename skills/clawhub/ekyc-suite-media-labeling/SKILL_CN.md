# eKYC Suite 图像标签

eKYC Suite Media Labeling 是母品牌 `eKYC Suite` 下的独立图像与视频标签 Skill，用于 KYC/eKYC 媒体风险复核、人物状态标签和场景标签。

运行：

```bash
python scripts/media_labeling.py --file <图片或视频> --labels "A02,A14" --type image
```

标签结果仅作为复核信号，不能替代人工判断或直接形成高影响决策。

## 权限与数据流

仅读取用户在命令中明确指定的图片或视频，以及 `EKYC_CLOUD_ENDPOINT`、`EKYC_CLOUD_API_KEY` 两个必要环境变量。媒体文件会发送到运营方配置的 HTTPS eKYC Suite Cloud 后端进行远程处理。仅可处理已获授权的媒体，并应实施最小留存、访问控制和人工复核；公开 Skill 本地不保存媒体或结果。

需求沟通：`carochen112233@gmail.com`
