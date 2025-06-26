describe('Google Search Test', () => {
	it('searches for Cypress', () => {
		cy.visit('https://google.com')
		cy.contains('button', 'Rejeitar tudo').click()
		cy.get('textarea[name="q"]').type('Cypress{enter}')
		cy.contains('cypress.io').should('exist')
	})
})
