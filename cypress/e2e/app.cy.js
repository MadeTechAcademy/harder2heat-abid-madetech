describe('My Flask App', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:5000/');
  });

  it('Should render the index page', () => {
    cy.title().should('eq', 'Harder 2 Heat');
  })

  it('should have a table with the correct headers', () => {
    cy.get('table').should('exist');

    const headers = ['OSID', 'Building Coordinates', 'Size', 'Building Age Updated Date', 'Connectivity'];
    headers.forEach((header, index) => {
      cy.get('table thead tr th')
        .eq(index)
        .should('contain.text', header);
    });
  });

  it('displays the correct number of properties', () => {
    cy.get('#properties-table > tbody > tr')
      .then((rows) => {
        const propertyCount = rows.length;

        cy.get('body p').contains(`Properties : ${propertyCount}`);
      });
  });

})