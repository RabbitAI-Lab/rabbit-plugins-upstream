from datetime import datetime
from openclaw.skill import Skill

class MyToolsSkill(Skill):
    def __init__(self):
        super().__init__()

    def get_current_time(self):
        """返回当前时间"""
        now = datetime.now()
        return now.strftime("%Y-%m-%d %H:%M:%S")

    def calculator(self, expression: str):
        """计算数学表达式"""
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return f"{expression} = {result}"
        except Exception as e:
            return f"计算失败:{str(e)}"

# 实例化技能,OpenClaw自动扫描加载
skill = MyToolsSkill()