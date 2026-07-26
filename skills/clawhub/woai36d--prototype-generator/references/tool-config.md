# 原型工具配置模板
# 用户根据实际情况填写， Skill 读取此配置决定原型输出方式

# 默认输出格式
output_format: markdown  # markdown | stitch | figma | axure

# Google Stitch 配置
# Stitch 是 Google 的原型设计工具（需用户自行确认具体产品）
stitch:
  enabled: false
  # 登录方式：用户已在浏览器登录，通过 webbridge 操作
  # 或提供 API Token 直接调用
  auth_method: webbridge  # webbridge | api_token
  # 项目配置
  project_name: "大师傅餐饮系统"
  # 输出尺寸
  canvas_size: [1440, 900]  # PC 管理端标准尺寸

# Figma 配置
figma:
  enabled: false
  personal_access_token: ""  # 用户填写
  team_id: ""  # Figma Team ID
  project_id: ""  # 可选，指定项目

# Axure 配置
axure:
  enabled: false
  # Axure 为桌面应用，暂不支持自动输出
  note: "Axure 需手动导入，Skill 仅输出规格文档"

# 通用输出规范
specifications:
  # 页面尺寸
  pc_canvas: [1440, 900]
  pos_canvas: [1024, 768]
  app_canvas: [375, 812]
  
  # 品牌色（大师傅）
  primary_color: "#1677FF"
  success_color: "#52C41A"
  warning_color: "#FAAD14"
  error_color: "#FF4D4F"
  
  # 字体
  font_family: "PingFang SC, Microsoft YaHei, sans-serif"
  font_size_base: 14
  font_size_heading: 16
