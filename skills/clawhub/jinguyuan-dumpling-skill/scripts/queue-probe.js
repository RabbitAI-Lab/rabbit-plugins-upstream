#!/usr/bin/env node
// Phase A 探针 M8：绕过 latestOrder，用 queueOrderViewId 直打上游 queueOrderDetail
// 用途：验证上游接口本身是否认历史 ID（带终态 or 报错）
// 用法：node scripts/queue-probe.js <queueOrderViewId>

const { createPassport } = require('./passport');

const BASE_URL = 'https://m.dianping.com/queue/mdp/ajax/';

async function main() {
  const viewId = process.argv[2];
  if (!viewId) {
    console.error('用法: node scripts/queue-probe.js <queueOrderViewId>');
    process.exit(1);
  }

  const passport = createPassport();
  const cached = await passport.getToken();
  const token = cached?.token;
  if (!token) {
    console.error('无美团 token，请先 auth-start');
    process.exit(1);
  }

  const headers = {
    'User-Agent': 'MeituanQueue-Skill/2.0',
    Accept: 'application/json',
    enterchannel: '2',
    token
  };

  // 1. 先打 queueIndexV2 确认列表状态
  const indexUrl = new URL('queueIndexV2', BASE_URL);
  indexUrl.searchParams.set('dpShopId', '4211342');
  const indexResp = await fetch(indexUrl, { headers });
  const indexData = await indexResp.json();
  console.log('=== queueIndexV2 当前状态 ===');
  console.log(JSON.stringify(indexData, null, 2));

  // 2. 直打 queueOrderDetail（历史 ID）
  const detailUrl = new URL('queueOrderDetail', BASE_URL);
  detailUrl.searchParams.set('queueOrderViewId', viewId);
  const detailResp = await fetch(detailUrl, { headers });
  const detailData = await detailResp.json();
  console.log('\n=== queueOrderDetail 直查（历史 ID） ===');
  console.log(JSON.stringify(detailData, null, 2));
}

main().catch(e => { console.error(e); process.exit(1); });
