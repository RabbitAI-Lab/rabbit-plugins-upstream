---
version: 1.0
name: Midea-WCS-design-analysis
description: >
  Midea Smart Manufacturing WCS (Warehouse Control System) — an industrial-grade 
  warehouse management dashboard built on 美的集团 brand identity. Core aesthetic: 
  clean enterprise SaaS with 美的蓝 (#0092D8) as the sole chromatic anchor, Microsoft 
  YaHei (微软雅黑) as the unified typeface across all surfaces, white/light-gray canvas 
  for maximum readability in factory-floor lighting. Dense data tables for AGV fleet 
  management, real-time monitoring cards with status-indicating color coding 
  (green=running/yellow=waiting/red=error/blue=charging). Minimal decoration, 
  information-first layout optimized for 2560×1440 workstation displays with 
  responsive fallback to tablet (1024px) for mobile patrol.
colors:
  # Brand
  midea-blue: "#0092D8"
  midea-blue-hover: "#007ABF"
  midea-blue-active: "#0068A8"
  midea-blue-soft: "#E8F5FC"
  midea-blue-border: "#B3DFF5"
  # Canvas
  canvas: "#FFFFFF"
  canvas-soft: "#F7F9FB"
  canvas-strong: "#EFF2F5"
  # Ink
  ink: "#1A1A1A"
  body: "#4A4A4A"
  muted: "#8C8C8C"
  muted-soft: "#B8B8B8"
  # Hairlines
  hairline: "#E5E7EB"
  hairline-strong: "#D1D5DB"
  # Semantic (industrial status codes)
  success: "#52C41A"
  success-soft: "#F6FFED"
  success-border: "#B7EB8F"
  warning: "#FAAD14"
  warning-soft: "#FFFBE6"
  warning-border: "#FFE58F"
  error: "#FF4D4F"
  error-soft: "#FFF2F0"
  error-border: "#FFCCC7"
  info: "#1890FF"
  info-soft: "#E6F7FF"
  info-border: "#91D5FF"
  # AGV fleet states
  agv-running: "#52C41A"
  agv-waiting: "#FAAD14"
  agv-charging: "#1890FF"
  agv-error: "#FF4D4F"
  agv-idle: "#8C8C8C"
  # Chart palette (data visualization, 8-color safe)
  chart-1: "#0092D8"
  chart-2: "#52C41A"
  chart-3: "#FAAD14"
  chart-4: "#722ED1"
  chart-5: "#13C2C2"
  chart-6: "#EB2F96"
  chart-7: "#FA8C16"
  chart-8: "#2F54EB"
  # Selection
  selection-bg: "#0092D8"
  selection-fg: "#FFFFFF"
typography:
  # Microsoft YaHei (微软雅黑) — unified typeface
  # Rationale: 企业管控Windows环境，雅黑为系统预装字体，无需CDN/自托管
  display-xl:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 36px
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 32px
    letterSpacing: 0
  page-title:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 40px
    color: "#1578FF"
  section-title:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 24px
    color: "#1578FF"
  body-lg:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  body-md:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 22px
  body-sm:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  body-sm-strong:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 20px
  table-header:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 18px
  table-cell:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  caption:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 18px
  mono:
    fontFamily: "'Cascadia Mono', 'Consolas', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 20px
  button-md:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 22px
  button-sm:
    fontFamily: "'Microsoft YaHei', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 20px
  # ⚠️ PPT 规范映射（前端参考）
  # 封面主标题: 40pt bold → display-xl
  # 封面副标题: 28pt normal → display-lg
  # 页面标题: 32pt bold blue#1578FF → page-title
  # 表头: 11-12pt bold → table-header
  # 表格数据: 11pt → table-cell
  # 正文/风险: 10.5pt → body-sm
  # 最小字体: ≥10pt (≥13px)
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  pill: 9999px
  full: 9999px
  # Rationale: 工业系统偏保守，最大圆角 8px，不用大圆角/pill 除非按钮
spacing:
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  section: 80px
  # Rationale: 数据密集型 dashboard，间距紧凑但保持可读性
components:
  # Navigation
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    height: 56px
    padding: "0 {spacing.md}"
    logoColor: "{colors.midea-blue}"
  nav-link:
    textColor: "{colors.body}"
    activeTextColor: "{colors.midea-blue}"
    activeBorderColor: "{colors.midea-blue}"
    typography: "{typography.body-sm-strong}"
    padding: "{spacing.xs} {spacing.sm}"
  # Buttons
  button-primary:
    backgroundColor: "{colors.midea-blue}"
    textColor: "#FFFFFF"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    hoverBackgroundColor: "{colors.midea-blue-hover}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.midea-blue}"
    borderColor: "{colors.midea-blue-border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
    hoverBackgroundColor: "{colors.midea-blue-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "{spacing.xs} {spacing.sm}"
    hoverTextColor: "{colors.midea-blue}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "#FFFFFF"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.md}"
  # Cards
  card-default:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    shadow: "0 1px 3px rgba(0,0,0,0.08)"
  card-hover:
    shadow: "0 4px 12px rgba(0,146,216,0.12)"
    borderColor: "{colors.midea-blue-border}"
  stat-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
    valueTypography: "{typography.display-md}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  # Data Table
  data-table:
    headerBackgroundColor: "{colors.midea-blue}"
    headerTextColor: "#FFFFFF"
    headerTypography: "{typography.table-header}"
    cellTypography: "{typography.table-cell}"
    cellPadding: "{spacing.sm} {spacing.md}"
    rowHoverBackgroundColor: "{colors.midea-blue-soft}"
    stripeRowBackgroundColor: "{colors.canvas-soft}"
    borderColor: "{colors.hairline}"
    # ⚠️ 最小字体 ≥10pt (13px)，不低于此值
  # Status Badge
  badge-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    borderColor: "{colors.success-border}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-warning:
    backgroundColor: "{colors.warning-soft}"
    textColor: "{colors.warning}"
    borderColor: "{colors.warning-border}"
  badge-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    borderColor: "{colors.error-border}"
  badge-info:
    backgroundColor: "{colors.info-soft}"
    textColor: "{colors.info}"
    borderColor: "{colors.info-border}"
  # AGV Status Indicator
  agv-status-running:
    dotColor: "{colors.agv-running}"
    label: "执行中"
  agv-status-waiting:
    dotColor: "{colors.agv-waiting}"
    label: "待调度"
  agv-status-charging:
    dotColor: "{colors.agv-charging}"
    label: "充电中"
  agv-status-error:
    dotColor: "{colors.agv-error}"
    label: "异常"
  agv-status-idle:
    dotColor: "{colors.agv-idle}"
    label: "空闲"
  # Form
  form-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px {spacing.sm}"
    height: 36px
    focusBorderColor: "{colors.midea-blue}"
  form-label:
    typography: "{typography.body-sm-strong}"
    textColor: "{colors.body}"
  # Sidebar (WCS specific)
  sidebar:
    backgroundColor: "{colors.canvas-soft}"
    borderColor: "{colors.hairline}"
    width: 220px
    itemPadding: "{spacing.sm} {spacing.md}"
    itemTypography: "{typography.body-sm}"
    activeBackgroundColor: "{colors.midea-blue-soft}"
    activeTextColor: "{colors.midea-blue}"
    activeBorderLeft: "3px solid {colors.midea-blue}"
  # Monitoring Dashboard Panel
  monitor-panel:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    headerHeight: 40px
    headerBackgroundColor: "{colors.canvas-soft}"
    headerTypography: "{typography.body-sm-strong}"
    padding: "{spacing.md}"
patterns:
  layout:
    - name: "Dashboard Grid"
      description: "2560×1440 主屏，4-6 列响应式网格，stat-card 顶部 KPI 行，下方数据表格 + 图表"
      breakpoints:
        desktop: "2560px → 6列"
        laptop: "1920px → 4列"
        tablet: "1024px → 2列"
        mobile: "768px → 1列"
    - name: "Master-Detail"
      description: "左侧 AGV 列表/任务列表，右侧详情面板，可拖拽调整宽度"
    - name: "Real-time Monitor"
      description: "顶部 6 个 KPI stat-card，中部仓库热力图/AGV 位置图，底部任务队列表格"
  data-visualization:
    - name: "AGV Fleet Overview"
      chart: "散点图 + 状态色标，显示 AGV 在仓库中的实时位置"
      colors: "使用 agv-status-* 色系"
    - name: "Task Throughput"
      chart: "堆叠柱状图，按任务类型分解（入库/出库/盘点/充电）"
      colors: "使用 chart-1 ~ chart-4"
    - name: "Alert Timeline"
      chart: "水平甘特图，显示报警时间线和持续时长"
      colors: "error / warning 语义色"
interactions:
  hover:
    cardShadow: "0 4px 12px rgba(0,146,216,0.12)"
    borderColor: "{colors.midea-blue-border}"
    transition: "all 0.2s ease"
  active:
    buttonScale: 0.98
    transition: "transform 0.1s ease"
  focus:
    outline: "2px solid {colors.midea-blue}"
    outlineOffset: 2px
  loading:
    style: "skeleton"
    backgroundColor: "{colors.canvas-soft}"
    animationDuration: 1.2s
  refresh:
    style: "spin-icon"
    dataAutoRefresh: 5s
content-rules:
  language: "zh-CN (简体中文)，技术术语可保留英文缩写（AGV/WCS/MES/PLC）"
  tone: "专业、信息密集、无营销话术。工业系统不需要'赋能'和'生态'"
  naming:
    - "用操作者视角命名：'任务队列' 而非 'task_queue_view'"
    - "状态用主动语态：'执行中' 而非 'running_status'"
    - "报警描述：'3号AGV通讯超时' 而非 'Error: AGV_03 timeout'"
  numbers:
    - "KPI 数值用等宽字体（mono）方便对比"
    - "百分比保留1位小数，温度保留整数"
    - "大数字用千分位：1,234,567"
  empty-states:
    - "无任务时：'当前无待调度任务，所有 AGV 处于空闲状态'"
    - "无报警时：'系统运行正常，无未处理报警'"
accessibility:
  contrast:
    normal: "WCAG 2.1 AA ≥ 4.5:1"
    large: "WCAG 2.1 AA ≥ 3:1"
  keyboard: "所有交互元素支持 Tab 导航和 Enter/Space 激活"
  reduced-motion: "尊重 prefers-reduced-motion，关闭自动刷新以外的动画"
  language: "html lang='zh-CN'"
brand-notes:
  - "美的集团品牌标准色：#0092D8（RGB: 0, 146, 216）"
  - "所有对内工具系统统一使用此蓝色，不可使用其他主色"
  - "字体统一使用 Microsoft YaHei（微软雅黑），Windows 系统预装"
  - "PPT 最小字体不低于 10pt，前端映射为 13px"
  - "宣传材料对外发时需经吴晓飞审核"
---
