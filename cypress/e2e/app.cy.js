describe('My Flask App', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:5000/');
  });

  it('Should render the index page', () => {
    cy.get('body p').contains('Properties : 4');
  })

  it('should have a table with the correct headers', () => {
    cy.get('table').should('exist');

    const headers = ['OSID', 'Building Coordinates', 'Building Size', 'Building Age Updated Date', 'Connectivity'];
    headers.forEach((header, index) => {
      cy.get('table thead tr th')
        .eq(index)
        .should('contain.text', header);
    });
  });
})