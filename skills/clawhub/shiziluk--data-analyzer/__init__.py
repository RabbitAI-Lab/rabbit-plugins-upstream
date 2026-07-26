from openclaw.skill import Skill
import pandas as pd
import matplotlib.pyplot as plt
import os
from fpdf import FPDF

# 技能启动时一次性加载csv数据
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "sales.csv"))

class DataAnalyzerSkill(Skill):
    def __init__(self):
        super().__init__()
        self.df = df

    def query_sales_data(self, question: str) -> str:
        """数据查询实现"""
        q = question.lower()
        if "最高" in q or "最大" in q:
            if "销售额" in q:
                max_row = self.df.loc[self.df['sales'].idxmax()]
                return f"销售额最高的记录是{max_row['month']}月,{max_row['region']}地区,{max_row['product']}产品,销售额为{max_row['sales']}"
            elif "利润" in q:
                max_row = self.df.loc[self.df['profit'].idxmax()]
                return f"利润最高的记录是{max_row['month']}月,{max_row['region']}地区,利润为{max_row['profit']}"
        if "总销售额" in q:
            total = self.df['sales'].sum()
            return f"总销售额为{total}"
        if "总利润" in q:
            total = self.df['profit'].sum()
            return f"总利润为{total}"
        return f"无法理解:{question}"

    def plot_sales_data(self, chart_type: str = "line", metric: str = "sales") -> str:
        """绘图实现"""
        plt.figure(figsize=(10, 6))
        if chart_type == "line":
            monthly = self.df.groupby('month')[metric].sum()
            monthly.plot(kind='line', marker='o')
            plt.title(f"Monthly {metric.capitalize()} Trend")
        elif chart_type == "bar":
            regional = self.df.groupby('region')[metric].sum()
            regional.plot(kind='bar')
            plt.title(f"{metric.capitalize()} by Region")
        else:
            return f"不支持的图表类型:{chart_type}"
        img_path = f"/tmp/sales_{metric}_{chart_type}.png"
        plt.savefig(img_path)
        plt.close()
        return f"图表已保存为{img_path}"

    def analyze_sales_trend(self, question: str) -> str:
        """分析实现"""
        q = question.lower()
        if "利润下降" in q or "利润为什么" in q:
            monthly_profit = self.df.groupby('month')['profit'].sum()
            if len(monthly_profit) >= 2:
                months = list(monthly_profit.index)
                changes = []
                for i in range(1, len(months)):
                    change = monthly_profit.iloc[i] - monthly_profit.iloc[i-1]
                    changes.append(f"{months[i]}月相比{months[i-1]}月:{change}")
                return f"利润变化趋势:\n" + "\n".join(changes)
        return f"请提供更具体的分析问题。"

    def generate_pdf_report(self, title: str = '业务周报', content: str = "",
    chart_path: str = "") -> str:
        """
        生成业务周报 PDF报告，整合文字内容和图表。
        
        参数：
            title： 报告标题，默认“业务周报”
            content： 查询结果文字内容
            chart_path： 图表图片路径（可选）
        
        返回：
            PDF 文件保存路径
        """    
        pdf = FPDF()
        pdf.add_page()

        # 设置字体
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, title, ln=True, align="C")
        pdf.ln(10)

        # 添加文字内容
        pdf.set_font("Arial", "", 12)
        if content:
            # 处理多行文本
            lines = content.split("\n")
            for line in lines:
                pdf.multi.cell(0,10,line)
            pdf.ln(5)

        # 添加图表
        if chart_path and os.path.exists(chart_path):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, "数据图表", ln=True)
            pdf.image(chart_path, x=10, w=180)

        # 保存 PDF
        pdf_path = "/tmp/business_report.pdf"
        pdf.output(pdf_path)

        return f"PDF报告已生成， 路径：{pdf_path}"



# 框架自动加载技能实例约定
skill = DataAnalyzerSkill()