document.querySelector('#team-form').addEventListener('submit', (event) => {
  event.preventDefault();

  const teamName = document.querySelector('#team-name').value;
  const services = document.querySelector('#services').value;
  const contact = document.querySelector('#contact').value;

  const teamList = document.querySelector('#team-list');
  const teamCard = document.createElement('div');
  teamCard.className = 'team-card';
  teamCard.innerHTML = `
    <h3>${teamName}</h3>
    <p>${services}</p>
    <p>Contact: <a href="mailto:${contact}">${contact}</a></p>
  `;
  teamList.appendChild(teamCard);

  event.target.reset();
});

// Styles for dynamically added team cards
const style = document.createElement('style');
style.textContent = `
.team-card {
  border: 2px solid #FF7043;
  border-radius: 10px;
  padding: 1rem;
  background: rgba(255, 112, 67, 0.1);
  flex: 1 1 calc(33.333% - 1rem);
  box-sizing: border-box;
}

.team-card h3 {
  margin: 0 0 0.5rem;
}

.team-card p {
  margin: 0.5rem 0;
}
`;
document.head.appendChild(style);
