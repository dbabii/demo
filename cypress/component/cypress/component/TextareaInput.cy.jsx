import React from 'react'
import TextareaInput from '../../src/components/TextareaInput'

describe('TextareaInput', () => {
	it('renders and types', () => {
		const handleChange = cy.stub().as('onChange')
		cy.mount(<TextareaInput value="" onChange={handleChange} />)

		cy.get('textarea')
		  .should('have.attr', 'name', 'message')
		  .type('Hello, Cypress')

		cy.get('@onChange').should('have.been.called')
	})
})
