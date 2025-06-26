describe('Login Form', () => {
	it('submits the login form', () => {
		cy.visit('http://localhost:3000')
		//cy.get('#username').type('admin')
		//cy.get('#password').type('secret')
		cy.fixture('user').then(user => {
			cy.get('#username').type(user.username)
			cy.get('#password').type(user.password)
		})
		cy.get('button[type="submit"]').click()
	})
})
