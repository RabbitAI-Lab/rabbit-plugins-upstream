import WebSocket from 'ws';
import http from 'http';

async function getToken() {
  return new Promise((resolve) => {
    http.get('http://localhost:8765/token', (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          resolve(json.token);
        } catch {
          resolve('');
        }
      });
    }).on('error', () => resolve(''));
  });
}

async function runTests() {
  const token = await getToken();
  console.log(`Using token: ${token}`);

  const ws = new WebSocket(`ws://localhost:8765/bridge?token=${token}`);

  ws.on('open', () => {
    console.log('✅ Connected to bridge server');
    
    console.log('\n--- Test 1: ping ---');
    ws.send(JSON.stringify({ id: 1, type: 'ping', data: {} }));

    setTimeout(() => {
      console.log('\n--- Test 2: getPlatformInfo ---');
      ws.send(JSON.stringify({ id: 2, type: 'getPlatformInfo', data: {} }));
    }, 200);

    setTimeout(() => {
      console.log('\n--- Test 3: getPermissions ---');
      ws.send(JSON.stringify({ id: 3, type: 'getPermissions', data: {} }));
    }, 400);

    setTimeout(() => {
      console.log('\n--- Test 4: getMousePosition ---');
      ws.send(JSON.stringify({ id: 4, type: 'getMousePosition', data: {} }));
    }, 600);

    setTimeout(() => {
      console.log('\n--- Test 5: getScreenSize ---');
      ws.send(JSON.stringify({ id: 5, type: 'getScreenSize', data: {} }));
    }, 800);

    setTimeout(() => {
      console.log('\n--- All tests done, closing ---');
      ws.close();
    }, 2000);
  });

  let responseCount = 0;
  ws.on('message', (data) => {
    const msg = JSON.parse(data.toString());
    if (msg.type === 'response') {
      responseCount++;
      const respData = msg.data || {};
      const result = respData.error ? `ERROR: ${respData.error}` : JSON.stringify(respData.result).slice(0, 200);
      console.log(`Response #${responseCount} (id=${respData.id}): ${result}`);
    } else if (msg.type === 'connected') {
      console.log('Server connected event:', msg.data);
    } else {
      console.log('Message:', msg.type, msg.data ? JSON.stringify(msg.data).slice(0, 100) : '');
    }
  });

  ws.on('error', (err) => {
    console.error('❌ Error:', err.message);
    process.exit(1);
  });

  ws.on('close', (code, reason) => {
    console.log('\n✅ Connection closed', code, reason.toString());
    process.exit(code === 1000 ? 0 : 1);
  });

  setTimeout(() => {
    console.error('❌ Timeout: tests took too long');
    process.exit(1);
  }, 5000);
}

runTests();
