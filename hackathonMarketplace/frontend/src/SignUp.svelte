<script>
    import { createEventDispatcher }from 'svelte';
    let email = '';
    let password = '';
    let sell = false;
    let error = '';
    let successMessage = '';

    const dispatch = createEventDispatcher();

    async function handleSignUp() {
        // Validates email
        if (!email.includes('@')) {
            error = 'Please enter a valid email address';
            return;
        }

        // Validates password
        if (password.length <= 5) {
            error = 'Password must be at least 6 characters long';
            return;
        }

        //checks if email ends with .edu or not
        const role = email.endsWith('.edu') ? 'student' : 'notStudent';

        //sending for backend
        const userData = {
            email: email,
            password: password,
            role: role
        };

    try {
            const response = await fetch('http://localhost:5000/signup', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userData)
            });

            const data = await response.json();

            if (data.success) {
                // Successful sign-up, display success message
                successMessage = 'Sign-up successful!';
                error = ''; // Clear error if sign-up is successful
            } else {
                // Handle error response from the server
                error = data.message || 'Error signing up';
            }
        } catch (err) {
            console.error('Error:', err);
            error = 'There was an error processing your signup.';
        }
    }

</script>

<main>
    <h1>Sign Up</h1>
    <form on:submit|preventDefault={handleSignUp}>
    <label>
        Email:
        <input type="email" bind:value={email} required >
    </label>
    <label>
        Password:
        <input type="password" bind:value={password} required >
    </label>
    <button type="submit">Sign Up</button>
    </form>
    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    {#if successMessage}
        <p style="color: green;">{successMessage}</p>
    {/if}


</main>

<style>
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    form {
        display: flex;
        flex-direction: column;
    }

</style>