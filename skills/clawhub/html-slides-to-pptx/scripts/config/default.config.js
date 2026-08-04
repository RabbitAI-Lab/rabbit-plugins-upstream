// default.config.js — 转换器全部可调项(唯一事实源)
// 冻结对象;项目级覆盖见 config/merge.js 与 convert.js 的 slides.config.json 加载。
// ⚠️ 任何默认值改动都会改变 29 页黄金基线的 L2 输出 —— 改默认值前必须先跑 golden verify 确认影响。
const config = {
  // 画布与版面:1920×1080 px ↔ 13.333×7.5 in(16:9)
  canvas: { width: 1920, height: 1080 },
  slide: { widthIn: 13.333, heightIn: 7.5 },
  layout: { name: "W16x9" },
  viewport: { width: 1920, height: 1080 },
  settleMs: 200, // 页面加载后等待字体/CSS 稳定的时间

  // 浏览器端提取参数(序列化传入页面)
  extract: {
    boldThreshold: 600,       // font-weight ≥ 此值 → PPTX 粗体
    singleLineFactor: 1.3,    // 盒高 ≤ 行高×此系数 → 判定单行
    defaultColorHex: "1A1A1A", // 取不到文字颜色时的兜底色
    // Phase 2 加固(测绘证实对旧 29 页零影响,默认开启):
    gridBlockifiesChildren: true, // H4:grid item 与 flex item 一样块级化递归,不拍平
    guardNestedObjects: true,     // H2:嵌套 data-object 的内层不重复提取(由外层 walk 到达)
  },

  // 截图还原(红线③:截图前隐藏文字,避免重影)
  // 隐藏全部文字,而非仅 textbox:方式 B/C 下文字可作为 shape 对象的子元素存在,
  // 任何可见文字都会被提取为原生文本框,因此截图里不应保留任何文字
  capture: {
    hideTextCss: "*{color:transparent !important; text-shadow:none !important;}",
    // 截图分辨率倍数(2026-07-27 起 2x ≈ 288dpi,投影/打印不糊):
    // 浏览器 deviceScaleFactor;clip 仍按 CSS px,贴回尺寸不变,仅位图像素密度提升。
    // 改回 1 可恢复旧行为;此开关改变 L2 内嵌图数据(基线已于当日重建)。
    scale: 2,
    // 截图格式(2026-07-27 P1):'png'(默认,矢量/文字边缘锐利) | 'jpeg'(照片型背景体积降 5-10×)
    imageType: "png",
    quality: 80, // 仅 imageType:'jpeg' 生效(0-100)
  },

  // 原生线性渐变(2026-07-27 D2 拍板):默认关。
  // 开启时(预计 P2 实施):extract 检测 linear-gradient → 渲染端 XML 后处理注入 a:gradFill,
  // 产出可编辑原生渐变形状(覆盖渐变条/渐变卡片高频场景);色停含透明度/hint 超集时回退截图。
  // 关闭时:渐变走 capture 截图路径(2x DPI),观感达标但不可编辑。
  // radial/conic-gradient 恒走截图,与本开关无关。
  nativeGradient: false,

  // P2 2.1 母版(2026-07-27):defineSlideMaster 承接重复页眉/页脚/页码。
  // 页码:每页右下角显示页码(仅当页数 > 1 时有意义)
  // 页脚:每页底部居中文字(如公司名/保密声明)
  // 页脚色:页脚文字颜色(默认灰色)
  // 开关关(false)时不创建母版,每页独立(旧行为)
  master: {
    pageNumbers: false,
    footer: "",
    footerColor: "999999",
  },

  // P2 2.8:增量缓存(默认开)。基于 HTML 内容 hash + config hash 缓存提取+截图结果,
  // 未变化页跳过浏览器交互。缓存目录:slides/.cache/(手动删除即清空)。
  // 设为 false 可关闭(如调试提取管线时)。
  incrementalCache: true,

  // 设计质量检查(2026-08-02 重构 D 期,仅 validate 使用;转换器不读)。
  // 访谈落 brief 时生成项目级 slides.config.json 的 design 键;tier 为空串 = 未配置,
  // 此时全部设计检查休眠(旧项目 validate 输出零变化)。
  // tier: "presentation"|"mixed"|"reading";minBodyPx: 字号绝对下限;
  // fillThreshold: 内容区利用率下限(0.85 → 内容带底 ≥ 约 850px);
  // airyPages: 豁免填充检查的 airy 页文件名(封面/分隔/大字观点/引用/收尾)。
  design: {
    tier: "",
    minBodyPx: 14,
    fillThreshold: 0.85,
    airyPages: [],
  },

  // 图标字体自动截图(2026-07-27 P1):命中下列字体族的文字元素整体转截图,
  // 避免 PPTX 端字体缺失导致 glyph 错字。命中子串即触发(大小写不敏感)。
  iconFonts: ["iconfont", "FontAwesome", "Material Icons", "material-icons", "Material+Icons"],

  // box-shadow 的固定近似(规范已声明为"近似浅阴影")
  shadow: { type: "outer", blur: 6, offset: 3, angle: 90, color: "000000", opacity: 0.25 },

  // 字体映射(2026-07-23 起默认开启,用户决策):中文 → Microsoft YaHei,西文/数字 → Arial。
  // PPTX 受众(Windows/Office)大多没装 Noto Sans SC / Inter,原字体名会随机回退;
  // 需要保留页面原字体名时,在项目级 slides.config.json 设 { "applyFontMap": false }。
  fontMap: {
    "Noto Sans SC": "Microsoft YaHei",
    "Inter": "Arial",
    "PingFang SC": "Microsoft YaHei",
  },
  applyFontMap: true,
};

module.exports = Object.freeze(config);
