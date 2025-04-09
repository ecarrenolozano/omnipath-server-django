SELECT interactions.source AS interactions_source,
interactions.target AS '
 'interactions_target, interactions.is_directed AS interactions_is_directed, '
 'interactions.is_stimulation AS interactions_is_stimulation, '
 'interactions.is_inhibition AS interactions_is_inhibition, '
 'interactions.consensus_direction AS interactions_consensus_direction, '
 'interactions.consensus_stimulation AS interactions_consensus_stimulation, '
 'interactions.consensus_inhibition AS interactions_consensus_inhibition, '
 'interactions.type AS interactions_type \n'
 'FROM interactions \n'
 'WHERE ((interactions.ncbi_tax_id_source = ANY (ARRAY[%(param_1)s]))
 OR '
 '(interactions.ncbi_tax_id_target = ANY (ARRAY[%(param_1)s]))) AND '
 '(interactions.is_directed IS %(is_directed_1)s) AND '
 '((interactions.dorothea_level && %(dorothea_level_1)s::VARCHAR[]) AND '
 '(interactions.dorothea_coexp OR interactions.dorothea_tfbs) OR '
 'interactions.omnipath OR interactions.collectri) AND (interactions.source != '
 'interactions.target)


pprint(str(list(service.interactions(
    datasets = ['dorothea', 'collectri', 'omnipath'],
    dorothea_levels = {'A', 'B', 'C'},
    dorothea_methods = ['coexp', 'tfbs'],
    format = 'query'))[0][0]))


 SELECT
    interactions.source AS interactions_source,
    interactions.target AS interactions_target,
    interactions.is_directed AS interactions_is_directed,
    interactions.is_stimulation AS interactions_is_stimulation,
    interactions.is_inhibition AS interactions_is_inhibition,
    interactions.consensus_direction AS interactions_consensus_direction,
    interactions.consensus_stimulation AS interactions_consensus_stimulation,
    interactions.consensus_inhibition AS interactions_consensus_inhibition,
    interactions.type AS interactions_type
FROM
    interactions
WHERE
    (
        interactions.ncbi_tax_id_source = ANY (ARRAY[%(param_1)s])
        OR interactions.ncbi_tax_id_target = ANY (ARRAY[%(param_1)s])
    )
    AND interactions.is_directed IS %(is_directed_1)s
    AND (
        (
            interactions.dorothea_level && %(dorothea_level_1)s::VARCHAR[]
            AND (interactions.dorothea_coexp OR interactions.dorothea_tfbs)
        )
        OR interactions.omnipath
        OR interactions.collectri
    )
    AND interactions.source != interactions.target;
