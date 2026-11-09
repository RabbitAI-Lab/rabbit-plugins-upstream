// Original portable watchlist state helper; only public news belongs in this state.
import topicConfig from './topics.json' with {type:'json'};
import {createHash} from 'node:crypto';
const POLICY=topicConfig.topics;
export const TOPICS=['deadlock','valorant','gaming','ai','companies','politics','youtube'];
export function normalizeItem(item,now=Date.now()) {
  if(!TOPICS.includes(item.topic) || typeof item.title!=='string' || item.title.length>240 ||
    !Array.isArray(item.facts) || item.facts.length<1 || item.facts.length>6 ||
    item.facts.some(f=>typeof f!=='string'||f.length>500)) throw Error('Invalid news item');
  const url=new URL(item.url);
  if(url.protocol!=='https:' || url.username || url.password || url.port ||
    /^(localhost|127\.|10\.|192\.168\.|169\.254\.|\[)/i.test(url.hostname)) throw Error('Public HTTPS source required');
  const hosts=POLICY.find(topic=>topic.id===item.topic)?.source_hosts;
  if(hosts && (!Array.isArray(hosts)||!hosts.includes(url.hostname)))throw Error('Official source required for this topic');
  url.hash=''; for(const key of [...url.searchParams.keys()]) if(/^(utm_|fbclid|gclid)/i.test(key)) url.searchParams.delete(key);
  const published=Date.parse(item.publishedAt);
  if(!Number.isFinite(published) || published>now+300000 || published<now-72*3600000) throw Error('Publication outside fresh window');
  const facts=item.facts.map(f=>f.trim().replace(/\s+/g,' '));
  return {topic:item.topic,title:item.title.trim(),url:url.href,publishedAt:new Date(published).toISOString(),facts,
    key:createHash('sha256').update(url.href).digest('hex'),
    fingerprint:createHash('sha256').update(facts.join(' ').toLowerCase().replace(/[^\p{L}\p{N}]/gu,'')).digest('hex')};
}
export function selectItems(items,state,now=Date.now()) {
  if(!Array.isArray(items)||items.length>20) throw Error('At most 20 candidates');
  const selected=[],excluded=[],keys=new Set();
  for(const raw of items) {
    let item;try {item=normalizeItem(raw,now);} catch {excluded.push({reason:'invalid_or_undated_or_stale'});continue;}
    if(keys.has(item.key)){excluded.push({reason:'duplicate_candidate'});continue;} keys.add(item.key);
    const old=state.reported[item.key];
    if(old && (old.fingerprint===item.fingerprint || Date.parse(item.publishedAt)<=Date.parse(old.publishedAt) ||
      typeof raw.materialChange!=='string' || raw.materialChange.trim().length<30)) {
      excluded.push({reason:'already_reported_or_change_unverified'});continue;
    }
    selected.push({...item,...(old?{materialChange:raw.materialChange.slice(0,500)}:{})});
    if(selected.length===5) break;
  }
  return {selected,excluded};
}
export function recordDelivered(state,pending,text,messageId) {
  if(!/^\d{17,20}$/.test(messageId??'')) throw Error('Actual delivery ID required');
  let count=0;
  for(const item of pending) if(text.includes(item.url)) {
    state.reported[item.key]={fingerprint:item.fingerprint,publishedAt:item.publishedAt,messageId,url:item.url,title:item.title,facts:item.facts};count++;
  }
  return count;
}
