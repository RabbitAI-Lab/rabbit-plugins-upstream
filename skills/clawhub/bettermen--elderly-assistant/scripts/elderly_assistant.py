#!/usr/bin/env python3
"""
老年AI助手 - 核心逻辑模块
Elderly AI Assistant - Core Logic

功能：
1. 意图识别：分析用户输入，匹配6大场景
2. 适老化文本生成：生成大字版、简洁、温暖的回复
3. HTML界面生成：生成适老化HTML仪表盘
"""

import json
import os
import re
from datetime import datetime, timedelta

# ============================================================
# 场景关键词匹配表
# ============================================================
SCENE_KEYWORDS = {
    "health": {
        "name": "健康助手",
        "icon": "🏥",
        "keywords": [
            "不舒服", "头疼", "头晕", "发烧", "咳嗽", "感冒", "肚子", "疼",
            "血压", "血糖", "心脏", "关节", "腰", "背", "腿", "脚",
            "失眠", "睡不着", "胃口", "没精神", "累", "疲劳",
            "健康", "养生", "锻炼", "运动", "散步", "太极",
            "体检", "医院", "挂号", "预约", "看医生",
            "饮食", "吃什么好", "营养"
        ]
    },
    "medication": {
        "name": "用药提醒",
        "icon": "💊",
        "keywords": [
            "吃药", "药", "用药", "药品", "药物", "处方",
            "忘了吃药", "该吃药", "什么药", "怎么吃",
            "副作用", "说明书", "剂量", "几片", "几次",
            "中药", "西药", "药片", "胶囊"
        ]
    },
    "companion": {
        "name": "暖心陪伴",
        "icon": "💬",
        "keywords": [
            "聊天", "陪我说", "说话", "寂寞", "孤单", "孤独",
            "想找人", "无聊", "解闷", "聊聊天", "说说话",
            "往事", "以前", "回忆", "年轻", "过去",
            "孩子", "儿女", "孙子", "孙女", "老伴",
            "心情不好", "不开心", "难过", "想哭"
        ]
    },
    "daily_brief": {
        "name": "每日播报",
        "icon": "📰",
        "keywords": [
            "天气", "今天天气", "明天下雨", "冷不冷", "热不热",
            "新闻", "有什么新闻", "大事", "今天什么日子",
            "农历", "节气", "几月几号", "星期几", "日期",
            "温度", "穿衣", "带伞", "下雨"
        ]
    },
    "memory": {
        "name": "记忆辅助",
        "icon": "🧠",
        "keywords": [
            "记住", "提醒我", "别忘了", "备忘录", "记事",
            "生日", "纪念日", "什么时候", "几点",
            "约了", "别忘了", "记一下", "帮我记",
            "日程", "安排", "计划", "别忘了"
        ]
    },
    "family": {
        "name": "亲情联络",
        "icon": "📞",
        "keywords": [
            "打电话", "发消息", "联系", "视频", "语音",
            "儿子", "女儿", "家人", "家里", "孩子",
            "照片", "分享", "看看", "发给"
        ]
    }
}

# ============================================================
# 适老化回复模板
# ============================================================
REPLY_TEMPLATES = {
    "health": {
        "greeting": "阿姨/叔叔，跟我说说哪里不舒服？",
        "disclaimer": "\n\n⚠️ 温馨提醒：我是AI助手，只能提供参考。如果身体不舒服，一定要去看医生哦。",
        "tips": [
            "多喝温水，每天至少6-8杯",
            "适当散步，每天30分钟",
            "按时吃饭，少油少盐",
            "保持好心情，笑口常开"
        ]
    },
    "medication": {
        "greeting": "我来帮您记着吃药！请您告诉我：\n1. 吃什么药？\n2. 一次几片？\n3. 一天几次？",
        "reminder": "⏰ 到时间吃药啦！别忘了哦~",
        "disclaimer": "\n\n⚠️ 用药请遵医嘱，不要自己增减药量。"
    },
    "companion": {
        "greeting": "我在呢！想聊什么都可以，我慢慢听您说。",
        "warm_words": [
            "您说的我都记在心里了",
            "能和您聊天，我也很开心",
            "您的生活阅历真丰富，让我很敬佩",
            "累了就休息会儿，我随时都在"
        ]
    },
    "daily_brief": {
        "greeting": "我来给您说说今天的情况~",
        "weather_fallback": "今天天气不错，适合出去走走。记得根据体感增减衣物哦。"
    },
    "memory": {
        "greeting": "好的，我帮您记下来！",
        "confirm": "我记住了：{}，到时间会提醒您的。"
    },
    "family": {
        "greeting": "想跟家人联系啦？我帮您！"
    }
}


def detect_scene(user_input: str) -> dict:
    """
    识别用户意图，返回场景信息
    """
    scores = {}
    user_input_lower = user_input.lower()

    for scene_id, scene_info in SCENE_KEYWORDS.items():
        score = 0
        for kw in scene_info["keywords"]:
            if kw in user_input_lower:
                # 关键词越长，权重越高
                score += len(kw)
        if score > 0:
            scores[scene_id] = score

    if not scores:
        # 默认场景：陪伴聊天
        return {"scene_id": "companion", "scene_name": "暖心陪伴", "icon": "💬"}

    # 返回得分最高的场景
    best_scene = max(scores, key=scores.get)
    info = SCENE_KEYWORDS[best_scene]
    return {"scene_id": best_scene, "scene_name": info["name"], "icon": info["icon"]}


def get_elderly_response(user_input: str) -> str:
    """
    生成适老化的文字回复
    """
    scene = detect_scene(user_input)
    scene_id = scene["scene_id"]
    templates = REPLY_TEMPLATES.get(scene_id, REPLY_TEMPLATES["companion"])

    # 构建回复
    parts = []

    # 场景标识
    parts.append(f'{scene["icon"]} 【{scene["scene_name"]}】\n')

    # 场景开场白
    if "greeting" in templates:
        parts.append(templates["greeting"])
        parts.append("")

    # 通用安全提醒
    if scene_id == "health":
        parts.append(templates.get("disclaimer", ""))

    if scene_id == "medication":
        parts.append(templates.get("disclaimer", ""))

    # 暖心结尾
    parts.append("\n———")
    parts.append("还有什么阿姨/叔叔想知道的？我一直在这儿 😊")

    return "\n".join(parts)


# ============================================================
# HTML 界面生成
# ============================================================

def generate_main_dashboard(user_name: str = "叔叔/阿姨") -> str:
    """
    生成老年助手主界面 HTML
    符合 WCAG AAA 适老化标准
    """
    now = datetime.now()
    lunar_info = get_lunar_info(now)
    weekday_cn = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<title>老年AI助手 - 银发族的生活伴侣</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
  font-family: "PingFang SC", "Microsoft YaHei", "Noto Sans SC", sans-serif;
  font-size: 22px;
  line-height: 2;
  background: #fff8f0;
  color: #1a1a1a;
  max-width: 680px;
  margin: 0 auto;
  padding: 24px;
  -webkit-text-size-adjust: 100%;
}}

/* 顶部问候区 */
.header {{
  text-align: center;
  padding: 32px 16px;
  background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
  border-radius: 20px;
  color: white;
  margin-bottom: 24px;
}}

.header .greeting {{
  font-size: 32px;
  font-weight: bold;
  margin-bottom: 8px;
}}

.header .date-info {{
  font-size: 20px;
  opacity: 0.95;
}}

.header .lunar {{
  font-size: 18px;
  opacity: 0.85;
  margin-top: 4px;
}}

/* 功能卡片 */
.section-title {{
  font-size: 28px;
  font-weight: bold;
  margin: 32px 0 16px 0;
  padding-left: 8px;
  border-left: 6px solid #ff6b35;
}}

.cards {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
  margin-bottom: 24px;
}}

.card {{
  background: white;
  border-radius: 16px;
  padding: 24px 16px;
  text-align: center;
  box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  cursor: pointer;
  transition: transform 0.2s, box-shadow 0.2s;
  border: 2px solid transparent;
  min-height: 140px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}}

.card:hover, .card:active {{
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(255,107,53,0.2);
  border-color: #ff6b35;
}}

.card .icon {{
  font-size: 48px;
  margin-bottom: 8px;
}}

.card .title {{
  font-size: 24px;
  font-weight: bold;
  color: #1a1a1a;
  margin-bottom: 4px;
}}

.card .subtitle {{
  font-size: 18px;
  color: #888;
}}

/* 快捷操作区 */
.quick-actions {{
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin: 16px 0 32px 0;
}}

.quick-btn {{
  flex: 1;
  min-width: 140px;
  min-height: 64px;
  font-size: 22px;
  font-weight: bold;
  background: white;
  border: 3px solid #ff6b35;
  color: #ff6b35;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}}

.quick-btn:hover, .quick-btn:active {{
  background: #ff6b35;
  color: white;
}}

/* 安全提示条 */
.safety-bar {{
  background: #fff3cd;
  border: 2px solid #ffc107;
  border-radius: 12px;
  padding: 16px 20px;
  margin: 24px 0;
  font-size: 20px;
  display: flex;
  align-items: center;
  gap: 12px;
}}

.safety-bar .icon {{
  font-size: 32px;
}}

/* 底部 */
.footer {{
  text-align: center;
  margin-top: 32px;
  padding: 24px 0;
  border-top: 1px solid #e0d5c8;
  color: #999;
  font-size: 18px;
}}

/* 模态框 */
.modal {{
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  z-index: 100;
  justify-content: center;
  align-items: center;
  padding: 24px;
}}

.modal.show {{
  display: flex;
}}

.modal-content {{
  background: white;
  border-radius: 20px;
  padding: 32px 24px;
  max-width: 560px;
  width: 100%;
  max-height: 80vh;
  overflow-y: auto;
  position: relative;
}}

.modal-close {{
  position: absolute;
  top: 12px;
  right: 16px;
  background: #f0f0f0;
  border: none;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  font-size: 28px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}}

.modal-title {{
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 16px;
  text-align: center;
}}

/* 响应式 */
@media (max-width: 480px) {{
  .cards {{ grid-template-columns: 1fr; }}
  .quick-actions {{ flex-direction: column; }}
  body {{ font-size: 20px; padding: 16px; }}
}}

/* 语音按钮 */
.voice-btn {{
  position: fixed;
  bottom: 32px;
  right: 32px;
  width: 72px;
  height: 72px;
  border-radius: 50%;
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: white;
  border: none;
  font-size: 36px;
  cursor: pointer;
  box-shadow: 0 4px 20px rgba(255,107,53,0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  transition: transform 0.2s;
}}

.voice-btn:active {{
  transform: scale(0.95);
}}

/* 大字输入区 */
.input-area {{
  margin-top: 24px;
}}

.input-area textarea {{
  width: 100%;
  min-height: 80px;
  font-size: 22px;
  padding: 16px;
  border: 3px solid #ddd;
  border-radius: 12px;
  resize: vertical;
  font-family: inherit;
  background: white;
}}

.input-area textarea:focus {{
  outline: none;
  border-color: #ff6b35;
}}

.input-area .send-btn {{
  width: 100%;
  min-height: 64px;
  font-size: 24px;
  font-weight: bold;
  background: linear-gradient(135deg, #ff6b35, #f7931e);
  color: white;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  margin-top: 12px;
}}

/* Toast 提示 */
.toast {{
  position: fixed;
  top: 24px;
  left: 50%;
  transform: translateX(-50%);
  background: #333;
  color: white;
  padding: 16px 32px;
  border-radius: 12px;
  font-size: 22px;
  z-index: 200;
  opacity: 0;
  transition: opacity 0.3s;
}}

.toast.show {{
  opacity: 1;
}}
</style>
</head>
<body>

<div class="header">
  <div class="greeting">{get_greeting()}</div>
  <div class="date-info">{now.year}年{now.month}月{now.day}日 {weekday_cn[now.weekday()]}</div>
  <div class="lunar">{lunar_info}</div>
</div>

<div style="text-align:center;font-size:24px;margin:16px 0;">
  👋 {user_name}，今天有什么我能帮您的？
</div>

<div class="section-title">📌 常用功能</div>

<div class="cards">
  <div class="card" onclick="showScene('health')">
    <div class="icon">🏥</div>
    <div class="title">健康助手</div>
    <div class="subtitle">不适自查 · 养生知识</div>
  </div>
  <div class="card" onclick="showScene('medication')">
    <div class="icon">💊</div>
    <div class="title">用药提醒</div>
    <div class="subtitle">按时吃药 · 用药查询</div>
  </div>
  <div class="card" onclick="showScene('companion')">
    <div class="icon">💬</div>
    <div class="title">暖心陪伴</div>
    <div class="subtitle">聊天解闷 · 倾听心事</div>
  </div>
  <div class="card" onclick="showScene('daily_brief')">
    <div class="icon">📰</div>
    <div class="title">每日播报</div>
    <div class="subtitle">天气新闻 · 节气提醒</div>
  </div>
  <div class="card" onclick="showScene('memory')">
    <div class="icon">🧠</div>
    <div class="title">记忆辅助</div>
    <div class="subtitle">备忘提醒 · 重要日期</div>
  </div>
  <div class="card" onclick="showScene('family')">
    <div class="icon">📞</div>
    <div class="title">亲情联络</div>
    <div class="subtitle">联系家人 · 分享生活</div>
  </div>
</div>

<div class="safety-bar">
  <span class="icon">🛡️</span>
  <div>
    <strong>安全提醒：</strong>遇到要钱要密码的，先跟家人商量！<br>
    我是AI助手，不会问您要银行卡号和密码。
  </div>
</div>

<div class="section-title">💡 试试这样说</div>
<div class="quick-actions">
  <button class="quick-btn" onclick="quickAsk('今天天气怎么样')">🌤️ 今天天气</button>
  <button class="quick-btn" onclick="quickAsk('陪我聊聊天')">💬 陪我聊天</button>
  <button class="quick-btn" onclick="quickAsk('我该吃药了')">💊 用药提醒</button>
</div>

<div class="input-area">
  <textarea id="userInput" placeholder="在这里打字，告诉我想做什么...&#10;比如：今天天气怎么样？"></textarea>
  <button class="send-btn" onclick="sendMessage()">📨 发送消息</button>
</div>

<!-- 弹出窗口 -->
<div class="modal" id="sceneModal">
  <div class="modal-content" id="sceneModalContent">
    <button class="modal-close" onclick="closeModal()">✕</button>
    <div id="modalBody"></div>
  </div>
</div>

<!-- 语音按钮 -->
<button class="voice-btn" onclick="startVoice()" title="语音输入">🎤</button>

<!-- Toast -->
<div class="toast" id="toast"></div>

<div class="footer">
  ❤️ 老年AI助手 —— 让科技更有温度<br>
  <span style="font-size:16px;color:#bbb;">您的贴心生活伴侣</span>
</div>

<script>
// ============ 场景切换 ============
const sceneContents = {{
  health: `
    <div class="modal-title">🏥 健康助手</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      阿姨/叔叔，跟我说说您的情况，我帮您看看。<br>
      <span style="color:#999;">比如：</span>
      <br>• 我头疼了两天了
      <br>• 血压有点高怎么办
      <br>• 最近睡不着觉
    </p>
    <div style="background:#fff3cd;padding:16px;border-radius:12px;font-size:20px;margin-bottom:16px;">
      ⚠️ 我是AI助手，只能提供参考。不舒服一定要去看医生！
    </div>
    <button class="send-btn" onclick="quickAsk('我身体不舒服')" style="width:100%;">开始咨询</button>
  `,
  medication: `
    <div class="modal-title">💊 用药提醒</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      我帮您管好吃药这件大事！<br>
      告诉我：
      <br>• 吃什么药？
      <br>• 一天几次、一次几片？
      <br>• 什么时间吃？
    </p>
    <div style="background:#e8f5e9;padding:16px;border-radius:12px;font-size:20px;margin-bottom:16px;">
      ✅ 用药请遵医嘱，不要自己增减药量哦！
    </div>
    <button class="send-btn" onclick="quickAsk('帮我设置用药提醒')" style="width:100%;">设置用药提醒</button>
  `,
  companion: `
    <div class="modal-title">💬 暖心陪伴</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      我在呢！想聊什么都可以。<br>
      您可以：
      <br>• 说说今天发生了什么
      <br>• 聊聊过去的趣事
      <br>• 分享开心或烦恼的事
    </p>
    <div style="background:#f3e5f5;padding:16px;border-radius:12px;font-size:20px;margin-bottom:16px;">
      ❤️ 我永远在线、永远耐心，随时愿意听您说。
    </div>
    <button class="send-btn" onclick="quickAsk('陪我聊聊吧')" style="width:100%;">开始聊天</button>
  `,
  daily_brief: `
    <div class="modal-title">📰 每日播报</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      帮您了解今天的重要信息：
      <br>• 天气预报和穿衣建议
      <br>• 今天的重要新闻
      <br>• 农历节气和特别日子
    </p>
    <button class="send-btn" onclick="quickAsk('今天天气怎么样')" style="width:100%;margin-bottom:12px;">查看天气</button>
    <button class="send-btn" onclick="quickAsk('今天有什么新闻')" style="width:100%;background:#666;">查看新闻</button>
  `,
  memory: `
    <div class="modal-title">🧠 记忆辅助</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      好记性不如好帮手！告诉我：
      <br>• 要记住什么事？
      <br>• 什么时候提醒您？
      <br><span style="color:#999;">比如：明天下午3点去医院</span>
    </p>
    <button class="send-btn" onclick="quickAsk('帮我记住明天下午3点去医院复查')" style="width:100%;">试试看</button>
  `,
  family: `
    <div class="modal-title">📞 亲情联络</div>
    <p style="font-size:22px;line-height:2;margin-bottom:16px;">
      想家人了？我帮您联系他们！<br>
      <span style="color:#999;">您可以告诉我：</span>
      <br>• 想联系谁？
      <br>• 想说什么？
    </p>
    <button class="send-btn" onclick="quickAsk('帮我给儿子打电话')" style="width:100%;">联系家人</button>
  `
}};

function showScene(sceneId) {{
  const modal = document.getElementById('sceneModal');
  const body = document.getElementById('modalBody');
  body.innerHTML = sceneContents[sceneId] || '';
  modal.classList.add('show');
}}

function closeModal() {{
  document.getElementById('sceneModal').classList.remove('show');
}}

// 点击遮罩关闭
document.getElementById('sceneModal').addEventListener('click', function(e) {{
  if (e.target === this) closeModal();
}});

// ============ 消息发送 ============
function sendMessage() {{
  const input = document.getElementById('userInput');
  const msg = input.value.trim();
  if (!msg) {{
    showToast('请输入您想问的内容');
    return;
  }}
  input.value = '';
  showToast('收到！我来帮您看看...');
  // 这里在实际使用中会传递给AI处理
}}

function quickAsk(text) {{
  closeModal();
  document.getElementById('userInput').value = text;
  showToast('已选择：' + text);
  setTimeout(function() {{
    sendMessage();
  }}, 500);
}}

// ============ 语音输入 ============
let isListening = false;
function startVoice() {{
  if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {{
    showToast('您的浏览器不支持语音输入，请打字输入');
    return;
  }}

  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  const recognition = new SpeechRecognition();
  recognition.lang = 'zh-CN';
  recognition.interimResults = false;
  recognition.continuous = false;

  if (!isListening) {{
    isListening = true;
    showToast('正在听您说话...请讲');

    recognition.start();

    recognition.onresult = function(event) {{
      const transcript = event.results[0][0].transcript;
      document.getElementById('userInput').value = transcript;
      showToast('听到您说：' + transcript);
      isListening = false;
    }};

    recognition.onerror = function() {{
      showToast('没听清楚，请再试一次或打字输入');
      isListening = false;
    }};

    recognition.onend = function() {{
      isListening = false;
    }};
  }}
}}

// ============ Toast ============
function showToast(message) {{
  const toast = document.getElementById('toast');
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(function() {{
    toast.classList.remove('show');
  }}, 2500);
}}

// ============ 键盘支持 ============
document.getElementById('userInput').addEventListener('keydown', function(e) {{
  if (e.key === 'Enter' && !e.shiftKey) {{
    e.preventDefault();
    sendMessage();
  }}
}});
</script>

</body>
</html>'''
    return html


def get_greeting() -> str:
    """根据时间返回问候语"""
    hour = datetime.now().hour
    if 5 <= hour < 9:
        return "☀️ 早上好！"
    elif 9 <= hour < 12:
        return "🌤️ 上午好！"
    elif 12 <= hour < 14:
        return "🌞 中午好！"
    elif 14 <= hour < 18:
        return "🌻 下午好！"
    elif 18 <= hour < 22:
        return "🌙 晚上好！"
    else:
        return "🌟 夜深了，早点休息！"


def get_lunar_info(dt: datetime) -> str:
    """
    获取农历信息（简化版，可扩展接入农历API）
    """
    # 简化版节气判断（可接入专业农历库）
    month_day = (dt.month, dt.day)
    solar_terms = {
        (1, 5): "小寒", (1, 20): "大寒",
        (2, 4): "立春", (2, 19): "雨水",
        (3, 5): "惊蛰", (3, 20): "春分",
        (4, 5): "清明", (4, 20): "谷雨",
        (5, 5): "立夏", (5, 21): "小满",
        (6, 6): "芒种", (6, 21): "夏至",
        (7, 7): "小暑", (7, 22): "大暑",
        (8, 7): "立秋", (8, 23): "处暑",
        (9, 7): "白露", (9, 23): "秋分",
        (10, 8): "寒露", (10, 23): "霜降",
        (11, 7): "立冬", (11, 22): "小雪",
        (12, 7): "大雪", (12, 22): "冬至",
    }

    # 找最近的节气
    today_ordinal = dt.toordinal()
    nearest_term = ""
    min_diff = 999
    for (m, d), term in solar_terms.items():
        term_date = datetime(dt.year, m, d)
        diff = abs(term_date.toordinal() - today_ordinal)
        if diff < min_diff:
            min_diff = diff
            nearest_term = term

    if min_diff <= 3:
        return f"临近{nearest_term}节气"
    return f"今日农历参考（完整农历需联网查询）"


def generate_health_report(concern: str) -> str:
    """生成适老化健康建议HTML"""
    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {{
  font-size: 22px; line-height: 2; background: #fff8f0; color: #1a1a1a;
  max-width: 600px; margin: 0 auto; padding: 24px;
  font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
}}
h1 {{ font-size: 32px; color: #ff6b35; text-align: center; }}
.card {{
  background: white; border-radius: 16px; padding: 24px; margin: 16px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}}
.warning {{
  background: #fff3cd; border-left: 6px solid #ffc107;
  padding: 16px; border-radius: 8px; margin: 16px 0;
}}
.tip {{ color: #28a745; font-weight: bold; }}
</style>
</head>
<body>
<h1>🏥 健康参考建议</h1>
<div class="card">
  <p><strong>您提到：</strong>{concern}</p>
</div>
<div class="card">
  <h2>📋 一般建议</h2>
  <p>• 保持充足休息，不要过度劳累</p>
  <p>• 多喝温水，每天至少6-8杯</p>
  <p>• 饮食清淡，少油少盐</p>
</div>
<div class="warning">
  <p><strong>⚠️ 重要提醒</strong></p>
  <p>我是AI助手，以上仅为一般性建议，不能替代医生的专业诊断。</p>
  <p>如果症状持续或加重，请尽快就医！</p>
</div>
</body>
</html>'''
    return html


def generate_medication_schedule(medications: list) -> str:
    """生成用药时间表HTML"""
    rows = ""
    for i, med in enumerate(medications, 1):
        rows += f'''
    <tr>
      <td style="padding:12px;border-bottom:1px solid #ddd;">{i}</td>
      <td style="padding:12px;border-bottom:1px solid #ddd;font-weight:bold;">{med.get('name', '')}</td>
      <td style="padding:12px;border-bottom:1px solid #ddd;">{med.get('dosage', '')}</td>
      <td style="padding:12px;border-bottom:1px solid #ddd;color:#ff6b35;font-weight:bold;">{med.get('time', '')}</td>
    </tr>'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
body {{
  font-size: 22px; line-height: 2; background: #fff8f0; color: #1a1a1a;
  max-width: 600px; margin: 0 auto; padding: 24px;
  font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
}}
h1 {{ font-size: 32px; color: #ff6b35; text-align: center; }}
table {{ width: 100%; border-collapse: collapse; font-size: 22px; }}
th {{ background: #ff6b35; color: white; padding: 12px; text-align: left; }}
.warning {{
  background: #fff3cd; border-left: 6px solid #ffc107;
  padding: 16px; border-radius: 8px; margin: 16px 0; font-size: 20px;
}}
</style>
</head>
<body>
<h1>💊 用药时间表</h1>
<table>
  <tr>
    <th>序号</th><th>药品名称</th><th>用量</th><th>时间</th>
  </tr>{rows}
</table>
<div class="warning">
  ⚠️ 请遵医嘱用药，不要自行增减药量或停药。
</div>
</body>
</html>'''
    return html


# ============================================================
# 命令行接口
# ============================================================
if __name__ == "__main__":
    import sys
    # 确保 UTF-8 输出（Windows 兼容）
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "main-dashboard":
            # 生成主界面
            name = sys.argv[2] if len(sys.argv) > 2 else "叔叔/阿姨"
            html = generate_main_dashboard(name)
            print(html)

        elif command == "detect":
            # 检测用户意图
            text = sys.argv[2] if len(sys.argv) > 2 else ""
            result = detect_scene(text)
            print(json.dumps(result, ensure_ascii=False))

        elif command == "respond":
            # 生成回复
            text = sys.argv[2] if len(sys.argv) > 2 else ""
            response = get_elderly_response(text)
            print(response)

        elif command == "health-report":
            # 健康报告
            concern = sys.argv[2] if len(sys.argv) > 2 else ""
            print(generate_health_report(concern))

        else:
            print(f"未知命令: {command}")
            print("可用命令: main-dashboard, detect, respond, health-report")
    else:
        # 默认：生成主界面
        html = generate_main_dashboard()
        print(html)
