// Инициализация всех неоновых эффектов
document.addEventListener('DOMContentLoaded', () => {
  // Активация кнопок
  document.querySelectorAll('.btn-neon').forEach(btn => {
    btn.addEventListener('mouseenter', () => {
      btn.style.transform = 'translateY(-3px)';
    });
  });
});

// Анимация неоновых кнопок
document.querySelectorAll('.neon-btn').forEach(btn => {
    btn.addEventListener('mouseenter', () => {
        btn.style.boxShadow = `0 0 15px var(--neon-blue), 0 0 30px rgba(5, 217, 232, 0.4)`;
    });

    btn.addEventListener('mouseleave', () => {
        btn.style.boxShadow = 'none';
    });
});

// GSAP анимации
gsap.from('.glass-card', {
    duration: 1,
    y: 50,
    opacity: 0,
    stagger: 0.1,
    ease: "power3.out"
});

