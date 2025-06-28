describe('My First Test', () => {
    it('Visit example page', () => { 
        cy.visit('https://example.cypress.io');
        cy.contains('type').click();
        // cy.pause();
        cy.url().should('include', '/commands/actions');
    });

    it('Fills out a form and submits it', () => {
    cy.visit('https://example.cypress.io/commands/actions');
    cy.get('.action-email').type('test@example.com');
    cy.get('.action-form').submit();
    });

    it('Intercepts and asserts a network request', () => {
        cy.intercept('GET', '**/comments/*').as('getComment');
        cy.visit('https://example.cypress.io/commands/network-requests');
        cy.get('.network-btn').click();
        cy.wait('@getComment').its('response.statusCode').should('eq', 200);
    })

    // it('logs in using custom command', () => {
    //     cy.visit('/login');
    //     cy.login('test@example.com', 'password123')
    // })

    it('uses a custome command to fill email field', () => {
        cy.visit('/commands/actions');
        cy.fillEmailField('test@example.com')
    })

    it('fills form with fixture data', () => {
        cy.visit('/commands/actions');
        cy.fixture('user').then((user) => {
            cy.get('.action-email').type(user.email);
        });
    })

    //as previous test but using async/await
    it('uses async/await with fixture data', async () => {
        const user = await cy.fixture('user');
        cy.visit('/commands/actions');
        cy.get('.action-email').type(user.email);
    })
});
