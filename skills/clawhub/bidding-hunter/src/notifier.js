#!/usr/bin/env node
/**
 * notifier.js — Notification dispatch for Bidding Hunter.
 *
 * Sends reports via configured notification channels.
 * Supports: stdout, file, webhook, feishu, dingtalk, slack.
 */

const fs = require('fs');
const path = require('path');
const { resolvePath } = require('./config');

/**
 * Dispatch a report to all configured notification channels.
 * @param {object} report - { text, json, markdown }
 * @param {object} config - Full config
 * @returns {Promise<Array>} Results per channel
 */
async function dispatch(report, config) {
  const channels = config.notifications?.channels || [];
  if (!channels.length) {
    // Default: stdout
    console.log(report.text);
    return [{ channel: 'stdout', status: 'ok' }];
  }

  const results = [];
  for (const channel of channels) {
    try {
      const result = await dispatchToChannel(report, channel, config);
      results.push({ channel: channel.type, status: 'ok', result });
    } catch (error) {
      results.push({ channel: channel.type, status: 'error', error: error.message });
      console.error(`[notifier] Failed to dispatch to ${channel.type}: ${error.message}`);
    }
  }
  return results;
}

async function dispatchToChannel(report, channel, config) {
  switch (channel.type) {
    case 'stdout':
      return sendStdout(report, channel);
    case 'file':
      return sendFile(report, channel, config);
    case 'webhook':
      return sendWebhook(report, channel);
    case 'feishu':
      return sendFeishu(report, channel);
    case 'dingtalk':
      return sendDingTalk(report, channel);
    case 'slack':
      return sendSlack(report, channel);
    default:
      throw new Error(`Unknown notification channel type: ${channel.type}`);
  }
}

function sendStdout(report, channel) {
  const format = channel.format || 'text';
  if (format === 'json') {
    console.log(JSON.stringify(report.json));
  } else if (format === 'markdown') {
    console.log(report.markdown);
  } else {
    console.log(report.text);
  }
  return 'ok';
}

function sendFile(report, channel, config) {
  const dir = channel.path || path.join(config.scan?.results_dir || '~/.bidding-hunter/scan_results', 'reports');
  const resolved = resolvePath(dir);
  fs.mkdirSync(resolved, { recursive: true });

  const date = report.json.date;
  const format = channel.format || 'json';

  let ext, content;
  if (format === 'markdown') {
    ext = 'md';
    content = report.markdown;
  } else if (format === 'text') {
    ext = 'txt';
    content = report.text;
  } else {
    ext = 'json';
    content = JSON.stringify(report.json, null, 2);
  }

  const filePath = path.join(resolved, `${date}.${ext}`);
  fs.writeFileSync(filePath, content, 'utf8');
  return filePath;
}

async function sendWebhook(report, channel) {
  const url = channel.webhook;
  if (!url) throw new Error('webhook URL is required');

  const payload = {
    report: report.json,
    text: report.text,
    markdown: report.markdown,
    timestamp: new Date().toISOString(),
  };

  const fetch = globalThis.fetch || require('node-fetch');
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(channel.headers || {}),
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error(`Webhook returned ${response.status}: ${await response.text().catch(() => '')}`);
  }
  return response.status;
}

/**
 * Feishu bot notification.
 * Uses Feishu bot webhook format with interactive card.
 */
async function sendFeishu(report, channel) {
  const webhook = channel.webhook;
  if (!webhook) throw new Error('feishu webhook URL is required');

  const json = report.json;
  const text = report.text;

  // Build Feishu card
  const card = buildFeishuCard(json, text, channel);

  const fetch = globalThis.fetch || require('node-fetch');
  const response = await fetch(webhook, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(card),
  });

  if (!response.ok) {
    const body = await response.text().catch(() => '');
    throw new Error(`Feishu webhook returned ${response.status}: ${body}`);
  }
  return response.status;
}

function buildFeishuCard(json, text, channel) {
  const elements = [];
  const newCount = json.added.length;

  // Header
  elements.push({
    tag: 'markdown',
    content: `**📋 Bid Intelligence — ${json.date}**\n${json.scan?.summary ? Object.entries(json.scan.summary).map(([k, v]) => `${k}: ${v}`).join(' | ') : ''}`,
  });

  // New matches
  if (newCount > 0) {
    elements.push({ tag: 'hr' });
    elements.push({
      tag: 'markdown',
      content: `**🆕 New Matches (${newCount})**`,
    });
    for (const e of json.added.slice(0, 10)) {
      elements.push({
        tag: 'markdown',
        content: `#${e.alias} [${e.level}] ${e.title.substring(0, 50)}  \n${e.region} · ${e.pub_date}  \n[View](${e.url})`,
      });
    }
    if (newCount > 10) {
      elements.push({
        tag: 'markdown',
        content: `... and ${newCount - 10} more`,
      });
    }
  }

  // Reminders
  if (json.reminders.urgent.length > 0) {
    elements.push({ tag: 'hr' });
    elements.push({
      tag: 'markdown',
      content: `**📌 Urgent Deadlines (${json.reminders.urgent.length})**`,
    });
    for (const r of json.reminders.urgent.slice(0, 5)) {
      const label = r.days === 0 ? '**TODAY**' : `${r.days}d`;
      elements.push({
        tag: 'markdown',
        content: `🔴 #${r.alias} ${r.title.substring(0, 40)} — ${label}`,
      });
    }
  }

  // Stats
  elements.push({ tag: 'hr' });
  const db = json.database;
  elements.push({
    tag: 'markdown',
    content: `📊 Total: ${db.total} | Tracked: ${db.byStatus?.tracked || 0} | Undecided: ${db.byStatus?.undecided || 0} | Discarded: ${db.byStatus?.discarded || 0}`,
  });

  return {
    msg_type: 'interactive',
    card: {
      header: {
        title: { tag: 'plain_text', content: `Bid Intelligence — ${json.date}` },
        template: 'blue',
      },
      elements,
    },
  };
}

async function sendDingTalk(report, channel) {
  const webhook = channel.webhook;
  if (!webhook) throw new Error('dingtalk webhook URL is required');

  const text = report.text;
  const payload = {
    msgtype: 'markdown',
    markdown: {
      title: `Bid Intelligence — ${report.json.date}`,
      text: report.markdown,
    },
  };

  const fetch = globalThis.fetch || require('node-fetch');
  const response = await fetch(webhook, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!response.ok) throw new Error(`DingTalk webhook returned ${response.status}`);
  return response.status;
}

async function sendSlack(report, channel) {
  const webhook = channel.webhook;
  if (!webhook) throw new Error('slack webhook URL is required');

  const payload = {
    text: `📋 Bid Intelligence — ${report.json.date}`,
    blocks: [
      {
        type: 'section',
        text: { type: 'mrkdwn', text: report.markdown },
      },
    ],
  };

  const fetch = globalThis.fetch || require('node-fetch');
  const response = await fetch(webhook, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  if (!response.ok) throw new Error(`Slack webhook returned ${response.status}`);
  return response.status;
}

module.exports = { dispatch };
