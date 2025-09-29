<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Sorteador de Itens</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0a1a2e; /* Azul escuro profundo */
      --card:#0f2336; /* Azul escuro para cards */
      --accent:#d4a017; /* Dourado suave */
      --muted:#a3bffa; /* Azul claro para textos secundários */
      --glass:rgba(255,255,255,0.06); /* Leve transparência */
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0; font-family:Inter,system-ui,Segoe UI,Roboto,"Helvetica Neue",Arial;
      background: radial-gradient(1200px 600px at 10% 10%, rgba(212,160,23,0.15), transparent),
                  linear-gradient(180deg,#081627 0%, #0b2a3f 100%);
      color:#e6eef8; -webkit-font-smoothing:antialiased; -moz-osx-font-smoothing:grayscale;
      display:flex; align-items:center; justify-content:center; padding:32px;
    }
    .container{width:960px; max-width:96%; display:grid; grid-template-columns:1fr 380px; gap:24px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
          border-radius:14px; padding:22px; box-shadow: 0 8px 30px rgba(2,6,23,0.6); border:1px solid rgba(255,255,255,0.03)}
    header{display:flex; align-items:center; gap:16px}
    .logo{width:56px; height:56px; border-radius:12px; background:linear-gradient(135deg,var(--accent),#f1c40f); display:flex; align-items:center; justify-content:center; font-weight:800; color:white; font-size:20px; box-shadow:0 6px 18px rgba(212,160,23,0.18)}
    h1{margin:0; font-size:18px}
    p.lead{margin:4px 0 0; color:var(--muted); font-size:13px}

    label{display:block; font-size:13px; margin-bottom:8px}
    .field{margin-top:12px}
    input[type=text], input[type=number], textarea, select{
      width:100%; padding:10px 12px; border-radius:10px; border:1px solid rgba(255,255,255,0.04);
      background:var(--glass); color:inherit; font-size:14px; outline:none; transition:box-shadow .18s, transform .08s;
    }
    textarea{min-height:120px; resize:vertical}
    .row{display:flex; gap:12px}
    .col{flex:1}
    .controls{display:flex; gap:12px; margin-top:14px}
    button.btn{padding:10px 14px; border-radius:10px; border:0; cursor:pointer; font-weight:600; font-size:14px}
    .btn-action{background:linear-gradient(90deg,var(--accent),#f1c40f); color:white; box-shadow:0 8px 24px rgba(7,11,26,0.6)}
    .btn-ghost{background:transparent; color:var(--muted); border:1px solid rgba(255,255,255,0.03)}

    aside{display:flex; flex-direction:column; gap:18px}
    .preview{display:grid; gap:12px}
    .result{height:220px; display:flex; align-items:center; justify-content:center; border-radius:12px; background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border:1px solid rgba(255,255,255,0.03)}
    .winner{font-size:28px; font-weight:800; letter-spacing:0.6px}
    .meta{color:var(--muted); font-size:13px; margin-top:6px}

    .list{max-height:180px; overflow:auto; padding:10px; border-radius:10px; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.02)}
    .person{padding:8px 10px; border-radius:8px; margin-bottom:8px; background:transparent; display:flex; justify-content:space-between; align-items:center}
    .person.highlight{background:linear-gradient(90deg, rgba(212,160,23,0.12), rgba(241,196,15,0.06)); transform:scale(1.02);}

    .log{max-height:180px; overflow:auto; padding:10px; border-radius:10px; background:rgba(255,255,255,0.02); border:1px solid rgba(255,255,255,0.02)}
    .log-entry{padding:8px 10px; border-radius:8px; margin-bottom:8px; background:transparent; font-size:13px}

    .small{font-size:12px; color:var(--muted)}
    footer{margin-top:12px; color:var(--muted); font-size:12px}

    #confetti{position:fixed; left:0; top:0; pointer-events:none; width:100%; height:100%; z-index:60}

    @media (max-width:880px){
      .container{grid-template-columns:1fr;}
      aside{order:-1}
    }
  </style>
</head>
<body>
  <canvas id="confetti"></canvas>
  <div class="container">
    <div class="card">
      <header>
        <div class="logo">S</div>
        <div>
          <h1>Veja o ganhadores de cada item</h1>
          <p class="lead">Coloque o nome do item e sorteie entre um intervalo de pessoas ou cole nomes próprios.</p>
        </div>
      </header>

      <div class="field">
        <label for="item">Nome do item</label>
        <input id="item" type="text" placeholder="Ex.: Camiseta, Brinde, Voucher..." value="Kit Gamer" />
      </div>

      <div class="field row">
        <div class="col">
          <label for="min">Número mínimo de pessoas</label>
          <input id="min" type="number" min="1" value="1" />
        </div>
        <div class="col">
          <label for="max">Número máximo de pessoas</label>
          <input id="max" type="number" min="1" value="10" />
        </div>
      </div>

      <div class="field">
        <label for="names">(Opcional) Cole nomes — um por linha</label>
        <textarea id="names" placeholder="João\nMaria\nCarlos (se preencher, o sorteio usará esses nomes)"></textarea>
      </div>

      <div class="controls">
        <button class="btn btn-action" id="drawBtn">Sortear agora</button>
        <button class="btn btn-ghost" id="clearBtn">Limpar</button>
      </div>

      <footer>
        Dica: se você colar nomes, os campos mínimo/máximo serão ignorados e o sorteio escolherá entre os nomes fornecidos.
      </footer>
    </div>

    <aside>
      <div class="card preview">
        <div class="result" id="resultBox">
          <div style="text-align:center">
            <div class="small">Item</div>
            <div class="winner" id="resultItem">—</div>
            <div class="meta" id="resultWinner">Pronto para sortear</div>
          </div>
        </div>

        <div>
          <div class="small" style="margin-bottom:8px">Lista de participantes</div>
          <div class="list" id="peopleList"></div>
        </div>

        <div>
          <div class="small" style="margin-bottom:8px">Histórico de sorteios</div>
          <div class="log" id="logList"></div>
        </div>
      </div>
    </aside>
  </div>

  <script>
    const itemInput = document.getElementById('item');
    const minInput = document.getElementById('min');
    const maxInput = document.getElementById('max');
    const namesArea = document.getElementById('names');
    const drawBtn = document.getElementById('drawBtn');
    const clearBtn = document.getElementById('clearBtn');
    const peopleList = document.getElementById('peopleList');
    const resultItem = document.getElementById('resultItem');
    const resultWinner = document.getElementById('resultWinner');
    const resultBox = document.getElementById('resultBox');
    const logList = document.getElementById('logList');

    let winnersLog = []; // Array para armazenar o histórico de sorteios

    function renderList(arr, highlightIndex = -1){
      peopleList.innerHTML = '';
      for(let i=0;i<arr.length;i++){
        const div = document.createElement('div');
        div.className = 'person' + (i===highlightIndex ? ' highlight' : '');
        div.innerHTML = `<div>${arr[i]}</div><div class="small">#${i+1}</div>`;
        peopleList.appendChild(div);
      }
    }

    function renderLog(){
      logList.innerHTML = '';
      for(const entry of winnersLog){
        const div = document.createElement('div');
        div.className = 'log-entry';
        div.innerHTML = `<div>${entry.item} - Vencedor: ${entry.winner} (${entry.date})</div>`;
        logList.appendChild(div);
      }
    }

    function buildParticipants(){
      const raw = namesArea.value.trim();
      if(raw){
        const byLine = raw.split(/\r?\n/).map(s=>s.trim()).filter(Boolean);
        return byLine;
      }
      let min = parseInt(minInput.value)||1;
      let max = parseInt(maxInput.value)||1;
      if(min<1) min=1;
      if(max<min) max = min;
      const arr = [];
      for(let i=min;i<=max;i++) arr.push('Pessoa ' + i);
      return arr;
    }

    function randomInt(maxExclusive){
      return Math.floor(Math.random()*maxExclusive);
    }

    function celebrate(){
      const canvas = document.getElementById('confetti');
      const ctx = canvas.getContext('2d');
      const W = canvas.width = window.innerWidth;
      const H = canvas.height = window.innerHeight;
      const pieces = [];
      for(let i=0;i<80;i++){
        pieces.push({x:W/2, y: H/3, vx:(Math.random()-0.5)*8, vy:(Math.random()*-6)-2, r:Math.random()*7+4, rot:Math.random()*360, vr:Math.random()*10-5})
      }
      let t=0;
      function frame(){
        t++; ctx.clearRect(0,0,W,H);
        for(const p of pieces){
          p.vy += 0.18; p.x += p.vx; p.y += p.vy; p.rot += p.vr;
          ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.rot*Math.PI/180);
          ctx.fillStyle = `hsl(${Math.floor(Math.random()*360)},70%,60%)`;
          ctx.fillRect(-p.r/2, -p.r/2, p.r, p.r*0.6);
          ctx.restore();
        }
        if(t<120) requestAnimationFrame(frame);
        else ctx.clearRect(0,0,W,H);
      }
      frame();
    }

    async function doDraw(){
      drawBtn.disabled = true; drawBtn.textContent = 'Sorteando...';
      const participants = buildParticipants();
      if(participants.length===0){
        alert('Nenhum participante válido. Informe nomes ou intervalo.');
        drawBtn.disabled = false; drawBtn.textContent = 'Sortear agora';
        return;
      }
      resultItem.textContent = itemInput.value.trim() || '—';
      renderList(participants);

      let chosenIndex = Math.floor(Math.random()*participants.length);
      const rounds = 24 + Math.floor(Math.random()*24);
      for(let i=0;i<rounds;i++){
        chosenIndex = (chosenIndex + 1 + Math.floor(Math.random()*3)) % participants.length;
        renderList(participants, chosenIndex);
        await new Promise(r=>setTimeout(r, 40 + i*6));
      }

      await new Promise(r=>setTimeout(r, 180));
      const winnerIndex = Math.floor(Math.random()*participants.length);
      renderList(participants, winnerIndex);

      const winner = participants[winnerIndex];
      resultWinner.textContent = `Vencedor: ${winner}`;
      resultBox.animate([{transform:'translateY(-8px)', boxShadow:'0 18px 60px rgba(0,0,0,0.6)'},{transform:'translateY(0)'}], {duration:420, easing:'cubic-bezier(.2,.9,.3,1)'});
      
      // Adicionar ao log
      const date = new Date().toLocaleString('pt-BR', {dateStyle:'short', timeStyle:'short'});
      winnersLog.push({item: itemInput.value.trim() || 'Item sem nome', winner, date});
      renderLog();

      celebrate();
      drawBtn.disabled = false; drawBtn.textContent = 'Sortear agora';
    }

    drawBtn.addEventListener('click', doDraw);
    clearBtn.addEventListener('click', ()=>{
      namesArea.value = '';
      minInput.value = 1; maxInput.value = 10;
      itemInput.value = '';
      resultItem.textContent = '—';
      resultWinner.textContent = 'Pronto para sortear';
      renderList([]);
      winnersLog = []; // Limpa o log
      renderLog();
    });

    // Atualizar preview quando inputs mudam
    [minInput, maxInput, namesArea, itemInput].forEach(el=>el.addEventListener('input', ()=>{
      const arr = buildParticipants(); renderList(arr);
      resultItem.textContent = itemInput.value.trim() || '—';
    }));

    // Redimensionar canvas de confetes
    window.addEventListener('resize', ()=>{
      const c = document.getElementById('confetti'); c.width = window.innerWidth; c.height = window.innerHeight;
    });

    // Inicializar lista e log
    renderList(buildParticipants());
    renderLog();
  </script>
</body>
</html>
