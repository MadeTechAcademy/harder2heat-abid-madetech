describe('template spec', () => {
  it('passes', () => {
    cy.visit('http://127.0.0.1:5000/')
    cy.contains('Properties : 4');
  })
})