from openclaw.skill import Skill
import pandas as pd
import matplotlib.pyplot as plt
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
# 技能启动时一次性加载csv数据
df = pd.read_csv(os.path.join(os.path.dirname(__file__), "sales.csv"))

class DataAnalyzerSkill(Skill):
    def __init__(self):
        super().__init__()
        self.df = df
        # 输出目录统一管理
        self.output_dir = "/tmp/sales_report"
        os.makedirs(self.output_dir, exist_ok=True)
        # 注册中文字体防止PDF乱码（环境有字体可按需替换）
        try:
            pdfmetrics.registerFont(TTFont('SimHei', 'SimHei.ttf'))
            self.font_name = "SimHei"
        except:
            self.font_name = "Helvetica"

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
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
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
        plt.savefig(img_path, dpi=150, bbox_inches="tight")
        plt.close()
        return img_path

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

    def export_sales_pdf_report(
        self,
        query_result: str,
        chart_paths: list[str],
        analysis_text: str,
        report_title: str = "销售业务周报",
        report_date_range: str = ""
    ) -> str:
        """
        整合查询文字、图表、深度分析生成业务周报PDF，返回PDF文件本地路径
        :param query_result: query_sales_data输出的统计文字结果
        :param chart_paths: plot_sales_data生成的图表文件路径列表
        :param analysis_text: analyze_sales_trend输出业务洞察文本
        :param report_title: 周报标题，可选
        :param report_date_range: 报表统计时间范围，可选
        :return: 生成完成的PDF绝对文件路径
        """
        # 生成唯一PDF文件名
        pdf_name = f"{report_title.replace(' ','_')}.pdf"
        pdf_path = os.path.join(self.output_dir, pdf_name)
        doc = SimpleDocTemplate(pdf_path, pagesize=A4)
        story = []
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        title_style.fontName = self.font_name
        normal_style = styles["Normal"]
        normal_style.fontName = self.font_name

        # 1. 封面标题
        title_para = Paragraph(report_title, title_style)
        story.append(title_para)
        story.append(Spacer(1, 20))
        if report_date_range:
            date_para = Paragraph(f"统计周期：{report_date_range}", normal_style)
            story.append(date_para)
        story.append(Spacer(1, 40))

        # 2. 数据统计板块
        story.append(Paragraph("一、销售数据统计", styles["Heading2"]))
        story.append(Spacer(1, 10))
        stat_para = Paragraph(query_result.replace("\n", "<br/>"), normal_style)
        story.append(stat_para)
        story.append(Spacer(1, 30))

        # 3. 图表板块，循环插入所有图表
        story.append(Paragraph("二、数据可视化图表", styles["Heading2"]))
        story.append(Spacer(1, 10))
        for img_path in chart_paths:
            if os.path.exists(img_path):
                img = Image(img_path, width=480, height=280)
                story.append(img)
                story.append(Spacer(1, 20))
            else:
                story.append(Paragraph(f"图表文件丢失：{img_path}", normal_style))
                story.append(Spacer(1, 10))

        # 4. 业务洞察板块
        story.append(Paragraph("三、深度业务分析", styles["Heading2"]))
        story.append(Spacer(1, 10))
        analysis_para = Paragraph(analysis_text.replace("\n", "<br/>"), normal_style)
        story.append(analysis_para)

        # 生成PDF文件
        doc.build(story)
        return pdf_path

# 框架自动加载技能实例约定
skill = DataAnalyzerSkill()