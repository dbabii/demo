import React from 'react'

const TextareaInput = ({ value, onChange}) => {
	return (
		<div>
		<label htmlFor="message">Message:</label>
		<textarea
			id="message"
			name="message"
			value={value}
			onChange={onChange}
			rows="4"
			cols="40"
		/>
		</div>
	)
}

export default TextareaInput
