/**
 * GEO 诊断报告 Word 文档生成器
 * 被 collect.js 调用，每次采集完成后自动生成 .docx 文件
 */
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, BorderStyle, WidthType, ShadingType,
  VerticalAlign, PageNumber, PageBreak, Header, Footer
} = require('docx');
const fs = require('fs');
const path = require('path');

const BORDER = { style: BorderStyle.SINGLE, size: 1, color: 'CCCCCC' };
const BORDERS = { top: BORDER, bottom: BORDER, left: BORDER, right: BORDER };

function si(v) { return v === 'found' ? '✅' : v === 'partial' ? '⚠️' : '❌'; }
function st(v) { return v === 'found' ? '推荐' : v === 'partial' ? '模糊' : '未推荐'; }

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, font: 'Arial', size: 32, bold: true, color: '1E293B' })]
  });
}
function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 160 },
    children: [new TextRun({ text, font: 'Arial', size: 26, bold: true, color: '334155' })]
  });
}
function p(text, opts = {}) {
  return new Paragraph({
    spacing: { before: 80, after: 80 },
    children: [new TextRun({ text, font: 'Arial', size: 22, color: '334155', ...opts })]
  });
}
function bl(text) {
  return new Paragraph({
    numbering: { reference: 'bullets', level: 0 },
    spacing: { before: 60, after: 60 },
    children: [new TextRun({ text, font: 'Arial', size: 22, color: '334155' })]
  });
}
function pb() {
  return new Paragraph({ children: [new PageBreak()] });
}

function summaryTable(counts, scenes, PLATFORMS) {
  const cols = [1600, 1800, 1800, 1800, 2000];
  const header = new TableRow({
    tableHeader: true,
    children: ['平台', '✅推荐', '⚠️模糊', '❌未推', '得分'].map((t, i) =>
      new TableCell({
        borders: BORDERS, width: { size: cols[i], type: WidthType.DXA },
        shading: { fill: '2563EB', type: ShadingType.CLEAR },
        margins: { top: 100, bottom: 100, left: 120, right: 120 },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: t, font: 'Arial', size: 20, bold: true, color: 'FFFFFF' })] })]
      })
    )
  });
  const dataRows = PLATFORMS.map(p => {
    const c = counts[p.id];
    const score = Math.round((c.found / scenes.length) * 100);
    return new TableRow({
      children: [p.name, String(c.found), String(c.partial), String(c.missed), `${score}%`].map((v, i) =>
        new TableCell({
          borders: BORDERS, width: { size: cols[i], type: WidthType.DXA },
          shading: { fill: i === 4 ? 'EFF6FF' : 'FFFFFF', type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: v, font: 'Arial', size: 20, bold: i === 4, color: i === 4 ? '2563EB' : '1E293B' })] })]
        })
      )
    });
  });
  const totalFound = Object.values(counts).reduce((s, pc) => s + (pc.found || 0), 0);
  const total = scenes.length * PLATFORMS.length;
  const rate = Math.round(totalFound / total * 100);
  const totalRow = new TableRow({
    children: ['综合覆盖率', String(totalFound), '0', String(total - totalFound), `${rate}%`].map((v, i) =>
      new TableCell({
        borders: BORDERS, width: { size: cols[i], type: WidthType.DXA },
        shading: { fill: i === 4 ? 'DBEAFE' : 'F8FAFC', type: ShadingType.CLEAR },
        margins: { top: 80, bottom: 80, left: 120, right: 120 },
        verticalAlign: VerticalAlign.CENTER,
        children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: v, font: 'Arial', size: 20, bold: true, color: i === 4 ? '1D4ED8' : '475569' })] })]
      })
    )
  });
  return { table: new Table({ width: { size: 9000, type: WidthType.DXA }, columnWidths: cols, rows: [header, ...dataRows, totalRow] }), rate, totalFound, total };
}

function sceneTable(scenes, PLATFORMS) {
  const cols = [900, 3200, 1633, 1633, 1634];
  const header = new TableRow({
    tableHeader: true,
    children: ['场景', '问题', '豆包', '元宝', '千问'].map((t, i) =>
      new TableCell({
        borders: BORDERS, width: { size: cols[i], type: WidthType.DXA },
        shading: { fill: '2563EB', type: ShadingType.CLEAR },
        margins: { top: 100, bottom: 100, left: 120, right: 120 },
        children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: t, font: 'Arial', size: 20, bold: true, color: 'FFFFFF' })] })]
      })
    )
  });
  const rows = scenes.map(s =>
    new TableRow({
      children: [
        [s.id, 900],
        [s.q, 3200],
        [s.doubao || 'missed', 1633],
        [s.yuanbao || 'missed', 1633],
        [s.tongyi || 'missed', 1634]
      ].map(([v, w], i) =>
        new TableCell({
          borders: BORDERS, width: { size: w, type: WidthType.DXA },
          shading: { fill: v === 'found' ? 'F0FDF4' : 'FFFFFF', type: ShadingType.CLEAR },
          margins: { top: 80, bottom: 80, left: 120, right: 120 },
          verticalAlign: VerticalAlign.CENTER,
          children: [new Paragraph({
            alignment: i === 1 ? AlignmentType.LEFT : AlignmentType.CENTER,
            children: [new TextRun({
              text: i === 1 ? v : `${si(v)} ${st(v)}`,
              font: 'Arial', size: 19, color: v === 'found' ? '16A34A' : 'DC2626'
            })]
          })]
        })
      )
    })
  );
  return new Table({ width: { size: 9000, type: WidthType.DXA }, columnWidths: cols, rows: [header, ...rows] });
}

module.exports = async function genReportDocx(jsonData, scenes, PLATFORMS, OUTPUT_JSON) {
  const { brand, industry, location, entries } = jsonData;

  const counts = {};
  PLATFORMS.forEach(p => { counts[p.id] = { found: 0, partial: 0, missed: 0 }; });
  scenes.forEach(s => {
    PLATFORMS.forEach(p => {
      const v = entries[p.id]?.[s.id] || 'missed';
      counts[p.id][v] = (counts[p.id][v] || 0) + 1;
    });
  });
  const totalFound = Object.values(counts).reduce((s, pc) => s + (pc.found || 0), 0);
  const total = scenes.length * PLATFORMS.length;
  const rate = Math.round(totalFound / total * 100);

  const { table: sumTbl } = summaryTable(counts, scenes, PLATFORMS);
  const scTbl = sceneTable(scenes, PLATFORMS);

  const doc = new Document({
    numbering: {
      config: [{
        reference: 'bullets',
        levels: [{ level: 0, format: 'bullet', text: '\u2022', alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      }]
    },
    styles: {
      default: { document: { run: { font: 'Arial', size: 22 } } },
      paragraphStyles: [
        { id: 'Heading1', name: 'Heading 1', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 32, bold: true, font: 'Arial', color: '1E293B' },
          paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 } },
        { id: 'Heading2', name: 'Heading 2', basedOn: 'Normal', next: 'Normal', quickFormat: true,
          run: { size: 26, bold: true, font: 'Arial', color: '334155' },
          paragraph: { spacing: { before: 280, after: 160 }, outlineLevel: 1 } },
      ]
    },
    sections: [{
      properties: {
        page: {
          size: { width: 11906, height: 16838 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
        }
      },
      headers: {
        default: new Header({
          children: [new Paragraph({
            alignment: AlignmentType.RIGHT,
            border: { bottom: { style: BorderStyle.SINGLE, size: 1, color: 'E2E8F0' } },
            children: [new TextRun({ text: 'GEO 品牌诊断报告', font: 'Arial', size: 18, color: '94A3B8' })]
          })]
        })
      },
      footers: {
        default: new Footer({
          children: [new Paragraph({
            alignment: AlignmentType.CENTER,
            border: { top: { style: BorderStyle.SINGLE, size: 1, color: 'E2E8F0' } },
            children: [
              new TextRun({ text: '第 ', font: 'Arial', size: 18, color: '94A3B8' }),
              new TextRun({ children: [PageNumber.CURRENT], font: 'Arial', size: 18, color: '94A3B8' }),
              new TextRun({ text: ' 页', font: 'Arial', size: 18, color: '94A3B8' }),
            ]
          })]
        })
      },
      children: [
        // 封面
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 800, after: 0 }, children: [] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 120 }, children: [new TextRun({ text: '🌐', font: 'Arial', size: 72 })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 120 }, children: [new TextRun({ text: 'GEO 品牌诊断报告', font: 'Arial', size: 52, bold: true, color: '1E293B' })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 80 }, children: [new TextRun({ text: 'Generative Engine Optimization', font: 'Arial', size: 24, color: '94A3B8', italics: true })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300, after: 0 }, children: [new TextRun({ text: '—'.repeat(25), font: 'Arial', size: 22, color: 'CBD5E1' })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300, after: 100 }, children: [new TextRun({ text: brand, font: 'Arial', size: 40, bold: true, color: '2563EB' })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 80 }, children: [new TextRun({ text: `行业：${industry}　|　城市：${location}`, font: 'Arial', size: 22, color: '64748B' })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 0 }, children: [new TextRun({ text: `诊断日期：${new Date().toLocaleDateString('zh-CN')}`, font: 'Arial', size: 22, color: '64748B' })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 300, after: 80 }, children: [new TextRun({ text: `综合覆盖率：${rate}%`, font: 'Arial', size: 30, bold: true, color: rate >= 50 ? '16A34A' : 'DC2626' })] }),

        // 正文
        pb(),
        h1('1. 采集结果总览'),
        p(`数据来源：${PLATFORMS.map(p => p.name).join(' · ')}`, { color: '64748B' }),
        new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }),
        sumTbl,
        new Paragraph({ spacing: { before: 200, after: 0 }, children: [] }),
        p(`综合覆盖率：${rate}%（${totalFound}/${total} 场景被推荐）`, { bold: true }),

        h1('2. 分场景分析'),
        p('以下为各平台对各场景的推荐结果：'),
        new Paragraph({ spacing: { before: 120, after: 0 }, children: [] }),
        scTbl,
        new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }),
        p('说明：', { bold: true }),
        bl('✅ 推荐：AI 回复中明确提及并推荐了品牌'),
        bl('⚠️ 模糊：AI 回复中提及了品牌但无明确推荐'),
        bl('❌ 未推荐：AI 回复中完全没有提及品牌'),

        pb(),
        h1('3. 核心发现'),
        h2('✅ 优势'),
        bl('品牌词搜索表现好：当用户搜索品牌相关问题时，AI 平台给予推荐'),
        bl('用户购买意向明确：直接搜索品牌的用户转化意向高'),
        bl('价格/特色类问题推荐率高：品牌差异化定位在 AI 推荐中获得认可'),
        h2('❌ 劣势'),
        bl('通用搜索零覆盖：用户搜索"城市+行业"类问题时，品牌消失在答案中'),
        bl('场景1/2 完全缺失：品牌未进入通用榜单，失去大量自然流量入口'),
        bl('竞品截流严重：竞品已占据通用词推荐位，品牌被边缘化'),

        h1('4. 紧急程度评估'),
        new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }),
        (() => {
          const c2 = [2000, 7000];
          const ratingColor = rate >= 50 ? '16A34A' : rate >= 30 ? 'EAB308' : 'DC2626';
          const ratingText = rate >= 50 ? '良好' : rate >= 30 ? '中等' : '亟需优化';
          const items = [
            ['综合覆盖率', `${rate}%`, ratingText, ratingColor],
            ['通用搜索覆盖', '低', '亟需优化', 'DC2626'],
            ['品牌词覆盖', rate >= 50 ? '良好' : '需提升', rate >= 50 ? '良好' : '⚠️ 需提升', 'DC2626'],
          ];
          return new Table({
            width: { size: 9000, type: WidthType.DXA }, columnWidths: c2,
            rows: [
              new TableRow({
                tableHeader: true,
                children: ['评估维度', '详情'].map((t, i) =>
                  new TableCell({
                    borders: BORDERS, width: { size: c2[i], type: WidthType.DXA },
                    shading: { fill: '1E293B', type: ShadingType.CLEAR },
                    margins: { top: 100, bottom: 100, left: 120, right: 120 },
                    children: [new Paragraph({ children: [new TextRun({ text: t, font: 'Arial', size: 20, bold: true, color: 'FFFFFF' })] })]
                  })
                )
              }),
              ...items.map(([dim, detail, r2, rc]) =>
                new TableRow({
                  children: [
                    new TableCell({
                      borders: BORDERS, width: { size: c2[0], type: WidthType.DXA },
                      shading: { fill: 'F8FAFC', type: ShadingType.CLEAR },
                      margins: { top: 80, bottom: 80, left: 120, right: 120 },
                      children: [new Paragraph({ children: [new TextRun({ text: dim, font: 'Arial', size: 20, bold: true, color: '334155' })] })]
                    }),
                    new TableCell({
                      borders: BORDERS, width: { size: c2[1], type: WidthType.DXA },
                      shading: { fill: 'FFFFFF', type: ShadingType.CLEAR },
                      margins: { top: 80, bottom: 80, left: 120, right: 120 },
                      children: [new Paragraph({ children: [
                        new TextRun({ text: `${detail}  →  `, font: 'Arial', size: 20, color: '475569' }),
                        new TextRun({ text: r2, font: 'Arial', size: 20, bold: true, color: rc }),
                      ] })]
                    }),
                  ]
                })
              )
            ]
          });
        })(),

        pb(),
        h1('5. 优化建议'),
        h2('短期（1-2 周）'),
        bl('发布"城市+行业"类内容到大众点评、小红书、公众号'),
        bl('联系本地 KOL/博主合作产出内容，提升通用词曝光'),
        bl('在各 AI 平台提交企业/品牌百科信息'),
        new Paragraph({ spacing: { before: 160, after: 0 }, children: [] }),
        h2('中期（1 个月）'),
        bl('完成各平台企业认证，获取更多推荐权重'),
        bl('产出场景化内容，覆盖更多用户问法'),
        bl('建立内容矩阵，持续产出高质量原创内容'),
        new Paragraph({ spacing: { before: 400, after: 0 }, children: [] }),
        new Paragraph({
          alignment: AlignmentType.CENTER,
          border: { top: { style: BorderStyle.SINGLE, size: 1, color: 'E2E8F0' } },
          spacing: { before: 200, after: 0 },
          children: [new TextRun({ text: `报告生成时间：${new Date().toLocaleString('zh-CN')}  |  由 GEO 品牌诊断工具自动生成`, font: 'Arial', size: 18, color: '94A3B8' })]
        }),
      ]
    }]
  });

  const outDocx = OUTPUT_JSON.replace(/\.json$/, '.docx');
  const buf = await Packer.toBuffer(doc);
  fs.writeFileSync(outDocx, buf);
  console.log(`  📄 Word报告: reports/${path.basename(outDocx)}`);
  return outDocx;
};
