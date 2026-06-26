const root = document.documentElement;
const themeToggle = document.querySelector('[data-theme-toggle]');
const toast = document.getElementById('toast');
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
let currentTheme = root.getAttribute('data-theme') || (prefersDark ? 'dark' : 'light');

function renderThemeIcon() {
  themeToggle.innerHTML = currentTheme === 'dark'
    ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>'
    : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
  themeToggle.setAttribute('aria-label', currentTheme === 'dark' ? 'Ativar modo claro' : 'Ativar modo escuro');
}

root.setAttribute('data-theme', currentTheme);
renderThemeIcon();

themeToggle.addEventListener('click', () => {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  root.setAttribute('data-theme', currentTheme);
  renderThemeIcon();
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('is-visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

function showToast(message) {
  toast.textContent = message;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2400);
}

document.querySelectorAll('[data-copy]').forEach(button => {
  button.addEventListener('click', async () => {
    const target = document.querySelector(button.dataset.copy);
    if (!target) return;
    try {
      await navigator.clipboard.writeText(target.textContent.trim());
      showToast('Chave Pix copiada.');
    } catch {
      showToast('Não foi possível copiar automaticamente.');
    }
  });
});

const leadForm = document.getElementById('leadForm');
leadForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(leadForm);
  const payload = Object.fromEntries(formData.entries());

  const summary = [
    'Olá, quero contratar o Start Digital – Kit Ouro.',
    `Nome: ${payload.nome || ''}`,
    `WhatsApp: ${payload.whatsapp || ''}`,
    `E-mail: ${payload.email || ''}`,
    `Instagram: ${payload.instagram || ''}`,
    `Segmento: ${payload.segmento || ''}`,
    `Cidade: ${payload.cidade || ''}`,
    `O que vende: ${payload.oferta || ''}`,
    `Objetivo: ${payload.objetivo || ''}`,
    `Concorrentes: ${payload.concorrentes || ''}`,
    `Dor principal: ${payload.dor || ''}`,
    'Pagamento: Pix'
  ].join('\n');

  const encoded = encodeURIComponent(summary);
  const waNumber = '5500000000000';
  window.open(`https://wa.me/${waNumber}?text=${encoded}`, '_blank', 'noopener,noreferrer');
  showToast('Briefing enviado. Finalize o pedido no WhatsApp.');
});
