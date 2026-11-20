import fs from 'node:fs';

export function diagnose(input) {
  if (!input || typeof input !== 'object' || typeof input.accountUrl !== 'string' || !input.accountUrl.trim()) {
    throw new Error('accountUrl 必填');
  }
  const works = Array.isArray(input.works) ? input.works.filter((item) => item && typeof item === 'object') : [];
  const numeric = (key) => works.map((item) => Number(item[key])).filter(Number.isFinite);
  const likes = numeric('likes');
  const comments = numeric('comments');
  const shares = numeric('shares');
  const views = numeric('views');
  const total = (values) => values.reduce((sum, value) => sum + value, 0);
  const rates = works.map((item) => {
    const view = Number(item.views);
    if (!Number.isFinite(view) || view <= 0) return null;
    return (Number(item.likes || 0) + Number(item.comments || 0) + Number(item.shares || 0)) / view;
  }).filter(Number.isFinite);
  const metrics = {
    sampleCount: works.length,
    totalLikes: total(likes),
    totalComments: total(comments),
    totalShares: total(shares),
    averageLikes: likes.length ? total(likes) / likes.length : null,
    averageComments: comments.length ? total(comments) / comments.length : null,
    averageShares: shares.length ? total(shares) / shares.length : null,
    averageEngagementRate: rates.length ? total(rates) / rates.length : null,
    viewsObserved: views.length
  };
  return {
    schemaVersion: '1.0',
    mode: input.mode === 'mock' ? 'mock' : 'real',
    capturedAt: input.capturedAt || new Date().toISOString(),
    account: { url: input.accountUrl, browserId: input.browserId || null },
    sample: works,
    metrics,
    findings: [],
    topicSuggestions: [],
    limitations: works.length ? [] : ['没有提供可见作品样本，无法计算样本指标。']
  };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const input = JSON.parse(fs.readFileSync(process.argv[2] || 0, 'utf8'));
  process.stdout.write(`${JSON.stringify(diagnose(input), null, 2)}\n`);
}
