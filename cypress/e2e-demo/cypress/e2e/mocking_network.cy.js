describe('Mocking Network Responses', () => {
    //GET request
    it('mock a GET request', () => {
        cy.intercept('GET', '/comments/*', {
            body: { id: 1, name: 'Test comment' },
        }).as('getComment');

        cy.visit('/commands/network-requests');
        cy.get('.network-btn').click();

        cy.wait('@getComment').its('response.body.name').should('eq', 'Test comment');
        });

    //POST request
    it('Mocks a POST request', () => {
        cy.intercept('POST', '**/comments').as('postComment');
        cy.visit('/commands/network-requests');
        cy.window().then((win) => {
            win.fetch('/comments', 
                { method: 'POST', body: JSON.stringify(
                    { text: 'Test Post'})
                });
        });
        cy.wait('@postComment').its('request.body').should('include', 'Test Post');
    });

})