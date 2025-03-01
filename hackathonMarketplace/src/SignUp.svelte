<script>
    let email = '';
    let password = '';
    let sell = false;
    export let onSignUp;
    function handleSignUp() {
        if (email.includes("uvm.edu")) {
            sell = true;
        }

        onSignUp();
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
        <input type="password" bind:value={email} required >
    </label>
    <button type="create"> Sign up </button>
    </form>
</main>