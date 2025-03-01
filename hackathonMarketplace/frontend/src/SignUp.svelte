<script>
    import { createEventDispatcher }from 'svelte';
    let email = '';
    let password = '';
    let sell = false;
    let error = '';

    const dispatch = createEventDispatcher();

    function handleSignUp() {
        
        if (!email.includes("@")) {
            error = 'Please enter a valid email address.'
            return;
        }
        if (password.length <= 5) 
        {
            error = 'Enter a password with atleast 6 characters'
            return;
        }
        if (email.includes("@uvm.edu")) {
            sell = true;
        }
        dispatch('signUp');
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