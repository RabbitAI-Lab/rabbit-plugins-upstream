const https = require('https');

const TEMPLATES = [
  { id: '181913649', name: 'Drake Hotline Bling' },
  { id: '112126428', name: 'Distracted Boyfriend' },
  { id: '129242436', name: 'Change My Mind' },
  { id: '87743020', name: 'Two Buttons' },
  { id: '93895088', name: 'Expanding Brain' },
  { id: '100777631', name: 'Is This a Pigeon?' },
  { id: '119139145', name: 'Blank Nut Button' },
  { id: '131087935', name: 'Running Away Balloon' },
  { id: '217743513', name: 'UNO Draw 25 Cards' },
  { id: '4087833', name: 'Waiting Skeleton' },
  { id: '1035805', name: 'Boardroom Meeting Suggestion' },
  { id: '91538330', name: 'Woman Yelling at Cat' },
  { id: '438680', name: 'Batman Slapping Robin' }
];

function getTemplates() { return TEMPLATES; }

function findTemplate(query) {
  const q = query.toLowerCase();
  return TEMPLATES.filter(t => t.name.toLowerCase().includes(q));
}

function generateMeme({ templateId, topText, bottomText, username, password } = {}) {
  return new Promise((resolve, reject) => {
    const u = username || process.env.IMGFLIP_USER || 'imgflip_hub';
    const p = password || process.env.IMGFLIP_PASS || 'imgflip_hub';
    const params = new URLSearchParams({
      template_id: templateId,
      text0: topText || '',
      text1: bottomText || '',
      username: u,
      password: p
    });
    const body = params.toString();
    const req = https.request({
      hostname: 'api.imgflip.com',
      path: '/caption_image',
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded', 'Content-Length': Buffer.byteLength(body) }
    }, res => {
      let data = '';
      res.on('data', c => data += c);
      res.on('end', () => {
        try {
          const r = JSON.parse(data);
          r.success ? resolve({ url: r.data.url, page_url: r.data.page_url }) : reject(new Error(r.error_message));
        } catch (e) { reject(e); }
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

module.exports = { getTemplates, findTemplate, generateMeme, TEMPLATES };
