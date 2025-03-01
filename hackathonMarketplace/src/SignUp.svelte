<script>
    import { createEventDispatcher } from "svelte";
    let email = '';
    let password = '';
    let sell = false;
    const dispatch = createEventDispatcher;
    function signUp() {
        if (onSignUp) {
            onSignUp();
        }
    }
    function handleSignUp() {
        let error = '';
        if (email.includes("uvm.edu")) {
            sell = true;
        }
        if (!email.includes("@")) {
            error = 'Please enter a valid email address.'
            return;
        }
        if (!password.length > 5) {
            error = 'Enter a password with atleast 6 characters'
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
    <button on:click={signUp}>Sign Up</button>
    </form>
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